#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Hilda.'''

show = Show(
    title='Hilda',
    brief_title='Hilda',
    seasons={
        1: {'color': '#6DA19D',
            'episodes': {
                'S1E1': 'The Hidden People',
                'S1E2': 'The Midnight Giant',
                'S1E3': 'The Bird Parade',
                'S1E4': 'The Sparrow Scouts',
                'S1E5': 'The Troll Rock',
                'S1E6': 'The Nightmare Spirit',
                'S1E7': 'The Lost Clan',
                'S1E8': 'The Tide Mice',
                'S1E9': 'The Ghost',
                'S1E10': 'The Storm',
                'S1E11': 'The House in the Woods',
                'S1E12': 'The Nisse',
                'S1E13': 'The Black Hound'}},
        2: {'color': '#FB6A5A',
            'episodes': {
                'S2E1': 'The Troll Circle',
                'S2E2': 'The Draugen',
                'S2E3': 'The Witch',
                'S2E4': 'The Eternal Warriors',
                'S2E5': 'The Windmill',
                'S2E6': 'The Old Bells of Trolberg',
                'S2E7': 'The Beast of Cauldron Island',
                'S2E8': 'The Fifty Year Night',
                'S2E9': 'The Deerfox',
                'S2E10': 'The Yule Lads',
                'S2E11': 'The Jorts Incident',
                'S2E12': 'The Replacement',
                'S2E13': 'The Stone Forest'}}},
    plot_threads=[
        ('S1E1', 'S1E2', Plot.SERIAL, "The elves trying to steal Hilda's home"),
        ('S1E2', 'S1E3', Plot.CAUSAL, "Hilda's new home in Trolberg"),
        ('S1E4', 'S1E5', Plot.CAUSAL, "The Troll rock"),
        ('S1E3', 'S1E10', Plot.REFERENTIAL, "The Great Raven"),
        ('S1E10', 'S1E11', Plot.SERIAL, "Hilda stranded in the woods"),
        ('S1E6', 'S1E12', Plot.REFERENTIAL, "The Marra"),
        ('S1E12', 'S1E13', Plot.SERIAL, "The Black Hound attacking Hilda and co."),
        ('S1E9', 'S2E2', Plot.REFERENTIAL, "The ghosts in the town graveyard"),
        ('S1E8', 'S2E3', Plot.REFERENTIAL, "The secret room in the library"),
        ('S1E10', 'S2E5', Plot.REFERENTIAL, "Victoria Van Gale"),
        ('S1E12', 'S2E5', Plot.REFERENTIAL, "The Nisse"),
        ('S1E7', 'S2E7', Plot.REFERENTIAL, "The Lindworm"),
        ('S2E6', 'S2E7', Plot.CAUSAL, "Ahlberg's automatic bells"),
        ('S2E7', 'S2E8', Plot.CAUSAL, "Hilda grounded"),
        ('S1E8', 'S2E11', Plot.CAUSAL, "The remaining Tide Mice"),
        ('S2E3', 'S2E11', Plot.REFERENTIAL, "The Witches Tower and Frieda learning magic"),
        ('S2E3', 'S2E13', Plot.CAUSAL, "Frieda learning magic"),
    ])
