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
                'S1E1': 'Chapter 1: The Hidden People',
                'S1E2': 'Chapter 2: The Midnight Giant',
                'S1E3': 'Chapter 3: The Bird Parade',
                'S1E4': 'Chapter 4: The Sparrow Scouts',
                'S1E5': 'Chapter 5: The Troll Rock',
                'S1E6': 'Chapter 6: The Nightmare Spirit',
                'S1E7': 'Chapter 7: The Lost Clan',
                'S1E8': 'Chapter 8: The Tide Mice',
                'S1E9': 'Chapter 9: The Ghost',
                'S1E10': 'Chapter 10: The Storm',
                'S1E11': 'Chapter 11: The House in the Woods',
                'S1E12': 'Chapter 12: The Nisse',
                'S1E13': 'Chapter 13: The Black Hound'}}},
    plot_threads=[
        ('S1E1', 'S1E2', Plot.SERIAL, "The elves trying to steal Hilda's home"),
        ('S1E2', 'S1E3', Plot.CAUSAL, "Hilda's new home in Trolberg"),
        ('S1E3', 'S1E4', Plot.CAUSAL, "The Troll rock"),
        ('S1E3', 'S1E10', Plot.REFERENTIAL, "The Great Raven"),
        ('S1E10', 'S1E11', Plot.SERIAL, "Hilda stranded in the woods"),
        ('S1E6', 'S1E12', Plot.REFERENTIAL, "The Marra"),
        ('S1E12', 'S1E13', Plot.SERIAL, "The Black Hound attacking Hilda and co.")])
