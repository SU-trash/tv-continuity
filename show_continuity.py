#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from enum import IntEnum
import json

import dateparser
# Fix strings that are just a year (e.g. "2020") from parsing as a valid date even when strict parsing is on
# Workaround per https://github.com/scrapinghub/dateparser/issues/751
dateparser.parser.no_space_parser_eligibile = lambda x: False
import pandas as pd
import wikipedia

import shows


class Plot(IntEnum):
    '''Enum representing the 'level' of an instance of plot continuity.
    Note: Re-appearance of an introduced character is not considered a plot point. Reuse of characters is considered
    baseline for even a fully episodic show (else it would be an anthology). A character may however reappear because
    of some ongoing goal of theirs (e.g. revenge), in which case their reappearance can be considered causal from e.g.
    the episode that caused them to want to take revenge.
    REFERENTIAL: The plot of Ep B is affected by a story element (thing, change in characters' relationship,
        skill learned by character, etc.) from ep A but is not 'directly' causally related to it nor is the
        conflict focused on it. Generally applies to changes to the 'status quo'. E.g. an episode in which two
        enemies become friends 'referentially' affects all future episodes in which they are shown being friends
        ('status quo' is updated from them being enemies to them being friends).
    CAUSAL: Ep A 'directly' causally relates to B, BUT the conflict in B is a conflict that was not present in A.
        Episode B's conflict would not exist without A or would be resolved differently based on a result of A.
        Also includes progression of ongoing 'arcs', e.g. if the episode includes discoveries about an ongoing mystery,
        or includes a significant change in a character's relationships (e.g. two enemies becoming friends is probably
        causal to future episodes focused on their relationship).
    SERIAL: Ep B addresses a problem created or progressed in A.
    '''
    REFERENTIAL = 1
    CAUSAL = 2  # + Arcs?
    SERIAL = 3


class Foreshadowing(IntEnum):
    '''Enum representing the 'level' of an instance of foreshadowing.
    Based on the (subjective) 'importance' of the subject being foreshadowed.
    In general it is considered minor if it foreshadows some detail of a single future episode, rather than a subject
    which will affect multiple episodes or major plot point resolutions.
    Note that instances of Chekhov's Gun are considered plot threads to be followed up on and not foreshadowing.
    '''
    MINOR = 1
    MAJOR = 2


def last(i):
    '''Helper for getting the last element of an iterable.'''
    try:
        return max(enumerate(i))[1]
    except ValueError:
        raise ValueError("last() arg is an empty sequence")

def numerify(s):
    '''Convert the given string to an integer if possible, else a float, else leave it as a string.'''
    cur = s
    try:
        cur = float(cur)
        if cur.is_integer():
            cur = int(cur)
    except ValueError:
        pass

    return cur

@dataclass
class Show:
    '''Data on a TV show and its continuity.'''
    title: str
    # Nested dicts structured as:
    # { season_id: {
    #     'color': season_color,
    #     'episodes' : {
    #         'S1E1': 'Title of episode 1',
    #         'S1E2-4': 'Title of multi-part episode'}}}
    seasons: dict
    plot_threads: list = field(default_factory=list)
    foreshadowing: list = field(default_factory=list)
    # A more compact title. Should also be unique so it can safely be used for file names
    brief_title: str = None

    def __post_init__(self):
        # This seems to be the only way to default to another field without abandoning @dataclass
        if self.brief_title is None:
            self.brief_title = self.title

        # Sanity checks on the inputted data
        eps = set(self.episodes())
        for ep_id in set(ep_id
                         for continuity_data in (self.plot_threads, self.foreshadowing)
                         for from_ep_id, to_ep_id, *_ in continuity_data
                         for ep_id in (from_ep_id, to_ep_id)):
            if ep_id not in eps:
                print(f'Warning: Unrecognized {self.brief_title} episode ID {ep_id}')

    def episodes(self):
        '''Return an iterable of the episodes from all seasons.'''
        return {ep: title for season in self.seasons for ep, title in self.seasons[season]['episodes'].items()}

    @classmethod
    def from_wikipedia(cls, title):
        # Possible column names that might contain the in-season ep number
        # We can't safely count episode numbers ourselves since some shows (typically those with two 10 min segments)
        # have e.g. ep 2a and 2b, but may also interleave full-length episodes (2a, 2b, 3, 4a, ...)
        ep_num_col_names = ['No. inseason', 'No.', 'Season Chapter']
        # TODO: Read title from page
        page = wikipedia.page(f'List of {title} episodes')
        print(f'Parsing episode list from {page.url}')
        tables = pd.read_html(page.html())
        seasons = {}
        cur_season = 0

        today = datetime.now()

        for table in tables:
            # TODO: Parse Seasons table
            # if 'Season' in table.keys():
            #     if 'Segments' in table.keys:  # Use this instead of Episodes if present
            #     cur_ep_num = 1
            #     for season_id, num_episodes in zip(table['Season'], table['Episodes']):
            #         # Store as int if possible
            #         if isinstance(season_id, str) and season_id.isdigit():
            #             season_id = int(season_id)
            #
            #         num_episodes = int(num_episodes)
            #
            #         seasons[season_id] = dict(from_ep=cur_ep_num, to_ep=cur_ep_num + num_episodes - 1,
            #                                   color='#000000')
            #         cur_ep_num += num_episodes

            # Parse episode titles from each season's table
            if (any(col_name in table.keys() for col_name in ep_num_col_names)
                    and any(' date' in k.lower() for k in table.keys())
                    and any('title' in k.lower() for k in table.keys())):
                # Add a new entry in the season dict
                cur_season += 1
                seasons[cur_season] = {'color': '#000000',
                                       'episodes': {}}

                # Get column names agnostically of variations in their formats (or of the presence of hyperlinks)
                ep_id_key = next(k for k in table.keys() if k in ep_num_col_names)
                title_key = next(k for k in table.keys() if 'title' in k.lower())
                release_date_key = next(k for k in table.keys() if ' date' in k.lower())

                for ep_id, ep_title, release_date_str in zip(table[ep_id_key],
                                                              table[title_key],
                                                              table[release_date_key]):
                    # Sanitize episode number/ID
                    # Strip hyperlink then convert to the simplest possible numeric type, else leave as string
                    ep_num = numerify(str(ep_id).split('[')[0])
                    # Ignore 'recap' episodes, e.g. '12.5'
                    if isinstance(ep_num, float):
                        continue

                    ep_id = f'S{cur_season}E{ep_num}'
                    # Some tables have double-length episodes formatted as two rows, ignore these
                    if ep_id in seasons[cur_season]['episodes']:
                        continue

                    # Sanitize title
                    if not isinstance(ep_title, str):
                        continue
                    # Extract the title from between quotes, ignoring extra info such as (Part 1) or hyperlinks
                    # When split on the " character, the episode's title(s) are every 2nd element after the first quote
                    ep_title = ' / '.join(ep_title.split('"')[1::2])

                    # Ignore un-aired episodes ('release date' in future or is 'TBA' or some such)
                    # This also filters out tables that have the episode description as every cell of the row
                    release_date_str = str(release_date_str).split('[')[0]  # Stringify and remove trailing hyperlinks
                    release_date = dateparser.parse(release_date_str, settings={'STRICT_PARSING': True})
                    if release_date is None or release_date > today:
                        continue

                    seasons[cur_season]['episodes'][ep_id] = ep_title

                # Ignore un-aired seasons
                seasons = {k: v for k, v in seasons.items() if v['episodes']}

        return cls(title=title, seasons=seasons)

    @classmethod
    def from_json_file(cls, json_file):
        '''Instantiate a Show from a JSON file.'''
        with open(json_file, 'r') as f:
            d = json.load(f)

            # Convert some data types back from the JSON limitations
            seasons = {numerify(k): v for k, v in d['seasons'].items()}

            plot_threads = [(from_ep, to_ep, Plot(level), description)
                            for from_ep, to_ep, level, description in d['plot-threads']]

            return cls(title=d['title'],
                       seasons=seasons,
                       plot_threads=plot_threads,
                       foreshadowing=d['foreshadowing'])

    def json(self):
        '''Return a JSON string of this object.'''
        return json.dumps({'title': self.title,
                           'seasons': self.seasons,
                           'plot-threads': self.plot_threads,
                           'foreshadowing': self.foreshadowing})

    def seriality_score(self, season=None):
        '''Return a metric from 0 to 1, where 0 is fully episodic and 1 is fully serial. Currently:
        (num_causal_eps + 1) / num_eps, or 0 if no causal eps
        This metric was chosen for satisfying all of the following 'nice'/'intuitive' properties:
        Note: 'episodic' below refers to all episodes that don't affect a future one, and subdivided by whether
              their plot was affected by a previous episode (plot-spawned vs non-plot-spawned)
        Note 2: In the below notation, each . is an episode (ordered left-to-right), and lines are causal connections
                between episodes. > < are also used mathematically which is hopefully not too confusing.
        . . = 0          (fully episodic shows give score 0)
        ._. = 1          (fully serial shows give score 1)
        ._. . = 2/3      (scale intuitive)
        . ._. = ._. .    (order-agnostic for isomorphic directed graphs)
        .<: = ._. .      (episodes which cause many other episodes cannot have an undue effect on the score)
        ._._.  >  .<:    (seriality worth more than plot-spawned episodic eps)
        .<:>. = ._._._.  (plot-spawned branches worth as much as serial if they converge again)
        .<.>. = ._._.    (alternate paths between already-causally-connected episodes do not change the score)
        Args:
            season: If not None, calculate seriality only for the given season's episodes (but including plot threads
                    to/from all seasons).
        '''
        if season is not None:
            assert season in self.seasons

            # Eps to calculate the seriality score of (E.g. Season 3)
            included_eps = set(self.seasons[season]['episodes'].keys())
        else:
            included_eps = self.episodes().keys()

        # If calculating for the overall show or the last season, the last episode cannot meaningfully be defined as
        # either causal or non-causal (barring time travel), so don't include it. Otherwise, the denominator is the
        # total number of episodes
        denominator = len(included_eps)
        if season is None or season == last(iter(self.seasons.keys())):
            denominator -= 1

        # If there are no future seasons to connect to, cannot meaningfully define causality
        if denominator <= 0:
            raise ZeroDivisionError(f"Cannot calculate seriality over {len(included_eps)} episode(s)")

        causal_eps = set(from_ep for from_ep, _, level, _ in self.plot_threads
                         if level >= Plot.CAUSAL
                         and from_ep in included_eps)

        # TODO: Flashbacks/time travel can currently over-inflate a show's score (.<->. . = 1, should be 0.5 imo)
        # Cap seriality to 1 in case the last episode does cause a previous episode
        return min(1, len(causal_eps) / denominator)

    def branching_factor(self, season=None):
        '''Return a score representing how much the show's plot branches, indicating the avg number of branches
        entering every caused episode. Uncaused episodes are ignored.
        E.g. In a 2 ep show, the score is 0 if it is episodic, 1 if it is serial, and 2+ if there are 2+ plot branches
        leading from the first episode to the second (or vice-versa).
        '''
        if season is not None:
            assert season in self.seasons

            # Eps to calculate the branching factor of (E.g. Season 3)
            included_eps = set(self.seasons[season]['episodes'].keys())

            # Eps to include plot threads to/from: all seasons up the target season (E.g. Seasons 1-3)
            known_eps = set()
            for cur_season, cur_season_dict in self.seasons.items():
                known_eps.update(cur_season_dict['episodes'].keys())

                if cur_season == season:
                    break
        else:
            known_eps = self.episodes().keys()
            included_eps = self.episodes().keys()

        # Identify plot threads that are causal to any episodes we are measuring
        causal_plot_threads = tuple((from_ep, to_ep) for from_ep, to_ep, level, _ in self.plot_threads
                                    if level >= Plot.CAUSAL  # Ignore referential plot threads
                                    and (from_ep in known_eps and to_ep in included_eps))

        caused_eps = set(to_ep for _, to_ep in causal_plot_threads)

        if not caused_eps:
            return 0
        else:
            return len(causal_plot_threads) / len(caused_eps)

    def print_plot_stats(self, indent=0):
        '''Print statistics on the plot threads present in the show. Currently a single summary statistic indicating
        the percent of seriality (as opposed to episodicity) in the show. See seriality_score().
        Args:
            indent: Indent the printed output this many spaces. Default 0.
        '''
        print(f'{indent * " "}Plot Seriality: {100 * self.seriality_score():.1f}%')
        if len(self.seasons) > 1:
            for season in self.seasons.keys():
                print(f'{indent * " "}Season {repr(season)}: {100 * self.seriality_score(season=season):.1f}%')

        print(f'\n{indent * " "}Plot Branching Factor: {self.branching_factor():.2f}')
        if len(self.seasons) > 1:
            for season in self.seasons.keys():
                print(f'{indent * " "}Season {repr(season)}: {self.branching_factor(season=season):.2f}')

    def print_foreshadowing_stats(self, season=None, indent=0, spoilers=False):
        '''Args:
            season: If not None, analyze only the given season and any foreshadowing to/from it. Default None.
            indent: Indent the printed output this many spaces. Default 0.
            spoilers: If True, include spoiler analystics. Default False.
        '''
        if season is not None:
            assert season in self.seasons

            # Eps to include foreshadowing to/from (E.g. Season 3)
            included_eps = set(self.seasons[season]['episodes'].keys())
        else:
            included_eps = self.episodes().keys()

        # Filter out foreshadowing to/from seasons we aren't including
        included_foreshadowing = tuple((from_ep, to_ep, *_) for from_ep, to_ep, *_ in self.foreshadowing
                                       if from_ep in included_eps or to_ep in included_eps)

        foreshadowing_eps = set(from_ep for from_ep, *_ in included_foreshadowing
                                if from_ep in included_eps)
        foreshadowed_eps = set(to_ep for _, to_ep, *_ in included_foreshadowing
                               if to_ep in included_eps)

        major_foreshadowing_eps = set(from_ep for from_ep, _, level, *_ in included_foreshadowing
                                      if from_ep in included_eps
                                      and level == Foreshadowing.MAJOR)
        major_foreshadowed_eps = set(to_ep for _, to_ep, level, *_ in included_foreshadowing
                                     if to_ep in included_eps
                                     and level == Foreshadowing.MAJOR)

        print(f"{indent * ' '}Avg foreshadowing per episode: {len(included_foreshadowing) / len(included_eps):.1f}")

        print(f"{indent * ' '}{100 * (len(foreshadowing_eps) / len(included_eps)):.1f}%"
              + " of episodes foreshadow a future episode")
        print(f"{indent * ' '}{100 * (len(major_foreshadowing_eps) / len(included_eps)):.1f}%"
              + " of episodes have major foreshadowing for a future episode")

        print(f"\n{indent * ' '}{100 * (len(foreshadowed_eps) / len(included_eps)):.1f}%" +
              " of episodes are foreshadowed by a past episode")
        print(f"{indent * ' '}{100 * (len(major_foreshadowed_eps) / len(included_eps)):.1f}%"
              + " of episodes have a major story element foreshadowed by a past episode")
        if foreshadowed_eps and spoilers:
            foreshadowed_revelations = Counter(revelation for *_, revelation in included_foreshadowing)
            revelation, foreshadowed_count = foreshadowed_revelations.most_common(1)[0]
            print(f"\n{indent * ' '}Most foreshadowed revelation: {revelation}" +
                  f"; foreshadowed {foreshadowed_count} times")

    def print_continuity_stats(self, spoilers=False):
        print(f'{self.brief_title} Continuity Statistics:')

        if len(tuple(self.episodes())) <= 1:
            print("    THERE IS AS YET INSUFFICIENT DATA FOR A MEANINGFUL ANSWER.")
            return

        self.print_plot_stats(indent=4)

        print()
        if self.foreshadowing:
            self.print_foreshadowing_stats(indent=4, spoilers=spoilers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_data_modules', nargs='*', type=str,
                        default=shows.__all__,
                        help="The python module(s) to import show data from, from the 'shows' package.")
    parser.add_argument('--spoilers', action='store_true',
                        help="Allow showing spoilers in continuity data summary.")
    args = parser.parse_args()

    shows = [__import__(f'shows.{show_module_name}', fromlist=[f'show']).show
             for show_module_name in args.show_data_modules]
    for show in shows:
        show.print_continuity_stats(spoilers=args.spoilers)
        print()

    if not args.spoilers:
        print("Note: Some analytics including spoilers were excluded; to include them add the --spoilers flag")
