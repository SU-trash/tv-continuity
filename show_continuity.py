#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from enum import IntEnum
import json

import dateparser
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
    # Dict containing the number of episodes per season
    # it is assumed that all episodes listed have aired in seasonal order (i.e. if S2 has any episodes, S1 must not
    # have less than its listed number of episodes)
    seasons: dict
    # Dict of episode numbers and titles. Double-length episodes are instead indexed with a string
    # containing all the episode numbers they take up, formatted as either "1-3" or "1/2"
    episodes: dict
    plot_threads: list = field(default_factory=list)
    foreshadowing: list = field(default_factory=list)
    # A more compact title. Should also be unique so it can safely be used for file names
    brief_title: str = None

    def __post_init__(self):
        # This seems to be the only way to default to another field without abandoning @dataclass
        if self.brief_title is None:
            self.brief_title = self.title

    @classmethod
    def from_wikipedia(cls, title):
        # TODO: Read title from page
        page = wikipedia.page(f'List of {title} episodes')
        tables = pd.read_html(page.html())
        seasons = {}
        episodes = {}

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
            if ('No.overall' in table.keys() or 'No.' in table.keys()
                    and any(' date' in k.lower() for k in table.keys())
                    and any('title' in k.lower() for k in table.keys())):
                # Get a column names agnostically of variations in their formats (or of the presence of hyperlinks)
                if 'No.overall' in table.keys():
                    ep_num_key = next(k for k in table.keys() if k == 'No.overall')
                else:
                    ep_num_key = next(k for k in table.keys() if k == 'No.')
                title_key = next(k for k in table.keys() if 'title' in k.lower())
                release_date_key = next(k for k in table.keys() if ' date' in k.lower())

                for ep_num, ep_title, release_date_str in zip(table[ep_num_key],
                                                              table[title_key],
                                                              table[release_date_key]):
                    # Sanitize episode number/ID
                    # Strip hyperlink then convert to the simplest possible numeric type, else leave as string
                    ep_num = str(ep_num).split('[')[0]
                    ep_num = numerify(ep_num)
                    # Ignore 'recap' episodes, e.g. '12.5'
                    if isinstance(ep_num, float):
                        continue
                    # Some tables have double-length episodes formatted as two rows, ignore these
                    if ep_num in episodes:
                        continue

                    # Sanitize title
                    if not isinstance(ep_title, str):
                        continue
                    ep_title = ep_title.split('[')[0]
                    # Strip any title quotes and reformat if an episode has multiple possible titles
                    ep_title = ep_title.strip('"')
                    ep_title.replace('""', ' / ')

                    # Ignore un-aired episodes ('release date' in future or is 'TBA' or some such)
                    # This also filters out tables that have the episode description as every cell of the row
                    release_date_str = release_date_str.split('[')[0]
                    release_date = dateparser.parse(release_date_str)
                    if release_date is None or release_date > today:
                        continue

                    episodes[ep_num] = ep_title

        return cls(title=title, seasons=seasons, episodes=episodes)

    @classmethod
    def from_json_file(cls, json_file):
        '''Instantiate a Show from a JSON file.'''
        with open(json_file, 'r') as f:
            d = json.load(f)

            # Convert some data types back from the JSON limitations
            seasons = {int(k): v for k, v in d['seasons'].items()}
            episodes = {(int(k) if k.isdigit() else k): v for k, v in d['episodes'].items()}

            plot_threads = [(from_ep, to_ep, Plot(level), description)
                            for from_ep, to_ep, level, description in d['plot-threads']]

            return cls(title=d['title'],
                       seasons=seasons,
                       episodes=episodes,
                       plot_threads=plot_threads,
                       foreshadowing=d['foreshadowing'])

    def json(self):
        '''Return a JSON string of this object.'''
        return json.dumps({'title': self.title,
                           'seasons': self.seasons,
                           'episodes': self.episodes,
                           'plot-threads': self.plot_threads,
                           'foreshadowing': self.foreshadowing})

    def seriality_score(self, season=None):
        '''Return a metric from 0 to 1, where 0 is fully episodic and 1 is fully serial. Currently:
        (1 * show_has_any_conn
         + sum_over_all_episodes(0.9 * has_forward_conn + 0.1 * has_backward_conn))
         / num_episodes
        Somewhat subjectively weighted (0.9 : 0.1) toward 'converging' story branches being more serial than
        'diverging' story branches.
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
            season: If not None, calculate seriality only for the given season's episodes, including plot threads
            to them from prior seasons but ignoring those affecting future seasons. Note that due to this a show's
            overall seriality is greater than the average of its seasons' serialities. E.g. season 1 might score 0%
            seriality if it is internally episodic but a future season continues off some of its episodes.
        '''
        if season is not None:
            assert season in self.seasons

            known_eps = set()  # Episodes to include plot threads to/from (E.g. Seasons 1-3)
            included_eps = set()  # Episodes to calculate the seriality score of (E.g. Season 3)

            eps_list = list(self.episodes.keys())  # For ease of referencing by index
            cur_ep_idx = 0
            for cur_season, cur_season_dict in self.seasons.items():
                next_ep_idx = cur_ep_idx + cur_season_dict['num_eps']
                cur_season_eps = eps_list[cur_ep_idx:next_ep_idx]
                known_eps.update(cur_season_eps)

                if cur_season == season:
                    included_eps.update(cur_season_eps)
                    break

                cur_ep_idx = next_ep_idx
        else:
            known_eps = self.episodes.keys()
            included_eps = self.episodes.keys()

        included_plot_threads = tuple((from_ep, to_ep) for from_ep, to_ep, level, _ in self.plot_threads
                                      if level >= Plot.CAUSAL
                                      and ((from_ep in included_eps and to_ep in known_eps)
                                           or (from_ep in known_eps and to_ep in included_eps)))

        # This is a bit hacky but allows for scores of 0 (if there are any plot threads an implicit + 1 is given
        # to make the metric intuitive, e.g. `. ._.` = 2/3)
        if not included_plot_threads:
            return 0

        causal_eps = set(from_ep for from_ep, _ in included_plot_threads
                         if from_ep in included_eps)

        total_causality = len(causal_eps)

        # TODO: The below code isn't agnostic of the fact that we don't include plot threads to future seasons
        if season is None or season == next(iter(self.seasons.keys())):
            # Bias the weight to account for the last ep being unable to be causal
            # This makes the metric more intuitive (imo), e.g. `. ._.` = 2/3
            total_causality += 1
        # If this is a season other than the first, the causal bonus will be provided if there is any connection to a
        # previous season.
        # This is somewhat hacky, but makes the per-season metric somewhat more intuitive imo
        # (namely, for e.g. a 2 episode second season, it gives the property: S1_. . = S1 ._. = 0.5)
        # TODO: This hand-waives away time travel...
        elif any((from_ep in known_eps and from_ep not in included_eps)
                 or (to_ep in known_eps and to_ep not in included_eps)
                 for from_ep, to_ep in included_plot_threads):
            total_causality += 1

        return total_causality / len(included_eps)

    def branching_factor(self, season=None):
        '''Return a score from representing how much the show's plot branches, indicating the avg number of branches
        entering every caused episode. Uncaused episodes are ignored.
        E.g. In a 2 ep show, the score is 0 if it is episodic, 1 if it is serial, and 2+ if there are 2+ plot branches
        leading from the first episode to the second (or vice-versa).
        '''
        if season is not None:
            assert season in self.seasons

            known_eps = set()  # Episodes to include plot threads to/from (E.g. Seasons 1-3)
            included_eps = set()  # Episodes to calculate the branching factor of (E.g. Season 3)

            eps_list = list(self.episodes.keys())  # For ease of referencing by index
            cur_ep_idx = 0
            for cur_season, cur_season_dict in self.seasons.items():
                next_ep_idx = cur_ep_idx + cur_season_dict['num_eps']
                cur_season_eps = eps_list[cur_ep_idx:next_ep_idx]
                known_eps.update(cur_season_eps)

                if cur_season == season:
                    included_eps.update(cur_season_eps)
                    break

                cur_ep_idx = next_ep_idx
        else:
            known_eps = self.episodes.keys()
            included_eps = self.episodes.keys()

        # Filter down to the plot threads that are causal to any episodes we are measuring
        included_plot_threads = tuple((from_ep, to_ep) for from_ep, to_ep, level, _ in self.plot_threads
                                      if level >= Plot.CAUSAL  # Ignore referential plot threads
                                      and (from_ep in known_eps and to_ep in included_eps))

        caused_eps = set(to_ep for _, to_ep in included_plot_threads
                         if to_ep in included_eps)

        if not caused_eps:
            return 0
        else:
            return len(included_plot_threads) / len(caused_eps)

    def print_plot_stats(self, indent=0):
        '''Print statistics on the plot threads present in the show. Currently a single summary statistic indicating
        the percent of seriality (as opposed to episodicity) in the show. See seriality_score().
        Args:
            season: If not None, analyze only the given season and any plot threads to it (but not from it to future
                seasons).
        '''
        print(f'{indent * " "}Plot Seriality:')
        print(f'{indent * " "}Overall: {100 * self.seriality_score():.1f}%')
        for season in self.seasons.keys():
            print(f'{indent * " "}Season {repr(season)}: {100 * self.seriality_score(season=season):.1f}%')

        print(f'\n{indent * " "}Plot Branching Factor:')
        print(f'{indent * " "}Overall: {self.branching_factor():.2f}')
        for season in self.seasons.keys():
            print(f'{indent * " "}Season {repr(season)}: {self.branching_factor(season=season):.2f}')

    def print_foreshadowing_stats(self, season=None, indent=0):
        '''Args:
            season: If not None, analyze only the given season and any foreshadowing to/from it.
        '''
        if season is not None:
            assert season in self.seasons

            included_eps = set()

            eps_list = list(self.episodes.keys())  # For ease of referencing by index
            cur_ep_idx = 0
            for cur_season, cur_season_dict in self.seasons.items():
                next_ep_idx = cur_ep_idx + cur_season_dict['num_eps']
                if cur_season == season:
                    included_eps.update(eps_list[cur_ep_idx:next_ep_idx])
                    break

                cur_ep_idx = next_ep_idx
        else:
            included_eps = self.episodes.keys()

        # Filter out foreshadowing to/from seasons we aren't including
        included_foreshadowing = tuple((from_ep, to_ep, level) for from_ep, to_ep, level, _ in self.foreshadowing
                                       if from_ep in included_eps or to_ep in included_eps)

        foreshadowing_eps = set(from_ep for from_ep, _, _ in included_foreshadowing
                                if from_ep in included_eps)
        foreshadowed_eps = Counter(to_ep for _, to_ep, _ in included_foreshadowing
                                   if to_ep in included_eps)

        major_foreshadowing_eps = set(from_ep for from_ep, _, level in included_foreshadowing
                                      if from_ep in included_eps
                                      and level == Foreshadowing.MAJOR)
        major_foreshadowed_eps = set(to_ep for _, to_ep, level in included_foreshadowing
                                     if to_ep in included_eps
                                     and level == Foreshadowing.MAJOR)

        print(f"{indent * ' '}Avg foreshadowing per episode: {len(included_foreshadowing) / len(included_eps):.1f}")

        print(f"{indent * ' '}{100 * (len(foreshadowing_eps) / len(included_eps)):.1f}%"
              + " of episodes foreshadow a future episode")
        print(f"{indent * ' '}{100 * (len(major_foreshadowing_eps) / len(included_eps)):.1f}%"
              + " of episodes have major foreshadowing for a future episode")
        print()

        print(f"{indent * ' '}{100 * (len(foreshadowed_eps) / len(included_eps)):.1f}%" +
              " of episodes are foreshadowed by a past episode")
        print(f"{indent * ' '}{100 * (len(major_foreshadowed_eps) / len(included_eps)):.1f}%"
              + " of episodes have a major story element foreshadowed by a past episode")
        if foreshadowed_eps:
            ep_num, foreshadowed_count = foreshadowed_eps.most_common(1)[0]
            print(f"{indent * ' '}Most foreshadowed: Episode {ep_num}: {self.episodes[ep_num]}" +
                  f"; foreshadowed {foreshadowed_count} times")

    def print_continuity_stats(self):
        print(f'{self.brief_title} Continuity Statistics:')

        if len(self.episodes) <= 1:
            print("    THERE IS AS YET INSUFFICIENT DATA FOR A MEANINGFUL ANSWER.")
            return

        self.print_plot_stats(indent=4)

        print()
        if self.foreshadowing:
            self.print_foreshadowing_stats(indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_data_modules', nargs='*', type=str,
                        default=shows.__all__,
                        help="The python module(s) to import show data from, from the 'shows' package.")
    args = parser.parse_args()

    shows = [__import__(f'shows.{show_module_name}', fromlist=[f'show']).show
             for show_module_name in args.show_data_modules]
    for show in shows:
        show.print_continuity_stats()
        print()
