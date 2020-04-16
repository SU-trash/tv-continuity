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

# - Plot edge thicknesses set based on 'level' of plot continuity
#   Vague Definitions:
#     - Lvl 0, Show setting/premise: E.g. Main cast of characters, common locations, etc.
#               Present across episodes in all shows except anthologies, can be ignored.
#     - Lvl 0.5, Callback: A previously introduced story element is re-referenced but does not 'affect' the plot. E.g.
#               recurring joke on a poster in background.
#     - Lvl 1, Referential: The plot of Ep B is affected by a story element (thing, change in characters' relationship,
#               skill learned by character, etc.) from ep A but is not 'directly' causally related to it nor is the
#               conflict focused on it. The element may help resolve the conflict.
#               Does not include story elements that are part of the 'main premise/setting' of the show, e.g.
#               main character or common location appearing.
#               This gets a bit subjective... feels something like how 'simple' it would be to accept the element
#               as a 'premise', e.g. I can accept 'character X has this superpower' but 'character X is in deep conflict
#               with Y due to past episode clashes' is not a 'simple premise'.
#     - Lvl 2, Causal: Ep A 'directly' causally relates to B, BUT the conflict in B is a new conflict that
#               was not present in A. Episode B's conflict would not exist without A or would be resolved differently
#               based on a result of A.
#               I feel like CB -> The Test belongs here, but the moon f. bracelet from SCI is only referential, this is
#               a bit subjective.
#     - Also lvl 2? Arc: Maybe same definition as causal?
#               'Hegehog uses magic she learnt' appearing in an episode would be Referential. I guess for
#               consistency to 'ongoing mysteries' - tidbits being dropped in otherwise unrelated episodes should be
#               referential, whereas if the mystery is a 'main focus' of the episode it would be Causal? But then how
#               can arcs escalate to Serial...
#     - Also lvl 2, Answer: Ep B answers or partly answers a mystery from ep A.
#     - Lvl 3, Serial: Ep B addresses a problem created or focused on in A.
#               E.g. fighting enemies that appeared at the end of A.
#   So e.g. an episode mainly focusing on Ramona/Susie's past would be Serial, if a tidbit about their past was
#   referenced that would be Causal/Arc (arc about their relationship), and an episode having Ramona merely appear
#   would be Referential? (since she's not a character from the show's original cast?)
#
# TODO: maybe need an indicator for when an episode changes the show's 'canon', i.e. it can be considered to affect
#       potentially any future episode involving the element it changed. This would include characters becoming friends,
#       skills learned, etc., but perhaps not include anything one would consider to be an arc and under plot focus.
#       For example, if several episodes were about MC attempting to befriend someone, that would be an 'arc' and merit
#       lvl 2 or above, but if an episode demonstrated two characters becoming friends and future episodes show them
#       being friends, this would be lvl 1 as the two characters being friends has become part of the show's
#       'baseline canon'.
#       For this category it perhaps doesn't make sense to have a line from 'X and Y become friends' to every episode
#       afterward in which they are shown being friends...
#       On the other hand e.g. Amity's introduction might merit starting a lvl 2 arc line following episodes in which
#       she has 'notable' character development or her relationship with Luz.
#       This is perhaps what I was intending with 'lvl 1 referential'...


class Plot(IntEnum):
    '''Enum representing the 'level' of an instance of plot continuity.'''
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


@dataclass
class Show:
    '''Data on a TV show and its continuity.'''
    title: str
    seasons: dict
    # Dict of episode numbers and titles. Double-length episodes are instead indexed with a string
    # containing all the episode numbers they take up, formatted as either "1-3" or "1/2"
    episodes: dict
    plot_threads: list = field(default_factory=list)
    foreshadowing: list = field(default_factory=list)
    callbacks: list = field(default_factory=list)

    @classmethod
    def from_wikipedia(cls, title):
        page = wikipedia.page(f'List of {title} episodes')
        tables = pd.read_html(page.html())
        seasons = {}
        episodes = {}

        today = datetime.now()

        for table in tables:
            # Parse Seasons table
            if 'Season' in table.keys():
                cur_ep_num = 1
                for season_id, num_episodes in zip(table['Season'], table['Episodes']):
                    print(type(season_id))
                    # Store as int if possible
                    if isinstance(season_id, str) and season_id.isdigit():
                        season_id = int(season_id)

                    num_episodes = int(num_episodes)

                    seasons[season_id] = dict(from_ep=cur_ep_num, to_ep=cur_ep_num + num_episodes - 1,
                                              color='#000000')
                    cur_ep_num += num_episodes

            # Parse episode titles from each season's table
            if 'No.overall' in table.keys() and any(' date' in k.lower() for k in table.keys()):
                # Get the air or release date column name
                release_date_key = next(k for k in table.keys() if ' date' in k.lower())

                for ep_num, ep_title, release_date_str in zip(table['No.overall'],
                                                              table['Title'],
                                                              table[release_date_key]):
                    # Ignore un-aired episodes ('release date' in future or is 'TBA' or some such)
                    release_date = dateparser.parse(release_date_str)
                    if release_date is None or release_date > today:
                        continue

                    # Ignore 'recap' episodes, e.g. '12.5'
                    # For some pages ep_num is parsed as a string and for others it is parsed as a numeric type
                    if '.' in str(ep_num):
                        continue

                    assert int(ep_num) not in episodes

                    # Strip title quotes and reformat if an episode has multiple possible titles
                    ep_title = ep_title.strip('"')
                    ep_title.replace('""', ' / ')

                    episodes[int(ep_num)] = ep_title

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
                       foreshadowing=d['foreshadowing'],
                       callbacks=d['callbacks'])

    def json(self):
        '''Return a JSON string of this object.'''
        return json.dumps({'title': self.title,
                           'seasons': self.seasons,
                           'episodes': self.episodes,
                           'plot-threads': self.plot_threads,
                           'foreshadowing': self.foreshadowing,
                           'callbacks': self.callbacks})

    def seriality_score(self):
        '''Return a metric from 0 to 1, where 0 is fully episodic and 1 is fully serial. Currently:
        (1 + sum_over_all_episodes(0.9 * has_forward_conn + 0.1 * has_backward_conn)) / num_episodes
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
        . ._. = ._. .    (order agnostic for isomorphic directed graphs)
        .<:  >  ._. .    (plot-spawned episodic eps are worth a bit more than non-plot-spawned episodic eps)
        .<:_. = ._.<:    (plot-spawned episodic eps are worth the same no matter when they appear)
        ._._.  >  :>.    (seriality worth more than non-plot-spawned branches)
        ._._.  >  .<:    (seriality worth more than plot-spawned episodic eps)
        .<:>. = ._._._.  (plot-spawned branches worth as much as serial if they converge again)
        .<.>. = ._._.    (alternate paths between already-causally-connected episodes do not change the score)
        '''
        # Weight attributed to episodes that causally affect a future episode
        # 0.5 would be symmetric between causal and caused episodes (e.g. F(.<:) = F(:>.))
        causal_weight = 0.9
        caused_weight = 1 - causal_weight
        causal_eps = set()
        caused_eps = set()

        for plot_thread in self.plot_threads:
            if len(plot_thread) == 3:
                from_ep, to_ep, _ = plot_thread
            else:
                from_ep, to_ep, level, _ = plot_thread
                if level < Plot.CAUSAL:
                    continue

            causal_eps.add(from_ep)
            caused_eps.add(to_ep)

        return (1 + causal_weight * len(causal_eps) + caused_weight * len(caused_eps)) / len(self.episodes)

    def print_plot_stats(self, indent=0):
        '''Print statistics on the plot threads present in the show. Currently a single summary statistic indicating
        the percent of seriality (as opposed to episodicity) in the show. See seriality_score().
        '''
        print(f'{indent * " "}Plot Seriality: {100 * self.seriality_score():.1f}%')

    def print_foreshadowing_stats(self, indent=0):
        foreshadowing_eps = set(from_ep for from_ep, _, _, _ in self.foreshadowing)
        foreshadowed_eps = Counter(to_ep for _, to_ep, _, _ in self.foreshadowing)

        major_foreshadowing_eps = set()
        major_foreshadowed_eps = set()
        for from_ep, to_ep, level, _ in self.foreshadowing:
            if level == Foreshadowing.MAJOR:
                major_foreshadowing_eps.add(from_ep)
                major_foreshadowed_eps.add(to_ep)

        print(f"{indent * ' '}{100 * (len(foreshadowing_eps) / len(self.episodes)):.1f}% of episodes foreshadow a future episode")
        print(f"{indent * ' '}{100 * (len(major_foreshadowing_eps) / len(self.episodes)):.1f}% of episodes have major foreshadowing for a future episode")
        print()

        print(f"{indent * ' '}{100 * (len(foreshadowed_eps) / len(self.episodes)):.1f}% of episodes are foreshadowed by a past episode")
        print(f"{indent * ' '}{100 * (len(major_foreshadowed_eps) / len(self.episodes)):.1f}% of episodes have a major story element foreshadowed by a past episode")
        if self.foreshadowing:
            ep_num, foreshadowed_count = foreshadowed_eps.most_common(1)[0]
            print(f"{indent * ' '}Most foreshadowed: Episode {ep_num}: {self.episodes[ep_num]}; foreshadowed {foreshadowed_count} times")

    def print_continuity_stats(self):
        print(f'{self.title} Continuity Statistics:')
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

    for show_module_name in args.show_data_modules:
        show = __import__(f'shows.{show_module_name}', fromlist=['show']).show

        show.print_continuity_stats()
        print()
