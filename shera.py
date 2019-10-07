#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''Data on the show She-Ra: Princesses of Power.'''

title = 'She-Ra'

# Dict of episode numbers and titles. Double-length episodes are instead indexed with a string
# containing all the episode numbers they take up, separated by forward slashes (/)
# Dicts are now conveniently ordered as of python 3.7 papa bless
episodes = {
    1: 'The Sword Part 1',
    2: 'The Sword Part 2',
    3: 'Razz',
    4: 'Flowers for She-Ra',
    5: 'The Sea Gate',
    6: 'System Failure',
    7: 'In the Shadows of Mystacor',
    8: 'Princess Prom',
    9: 'No Princess Left Behind',
    10: 'The Beacon',
    11: 'Promise',
    12: 'Light Hope',
    13: 'The Battle of Bright Moon',
    14: 'The Frozen Forest',
    15: 'Ties That Bind',
    16: 'Signals',
    17: 'S2E4', # The siege one?
    18: 'White Out',
    19: 'S2E6', # The Shadow weaver backstory one?
    20: 'S2E7', # The Bow's dads one
    21: 'The Price of Power',
    22: 'Huntara',
    23: 'Once Upon a Time in the Waste',
    24: 'Moment of Truth',
    25: 'Remember',
    26: 'The Portal'
}

# Season colors also set to match Wikipedia
# (Section colors from https://en.wikipedia.org/wiki/List_of_She-Ra:_Princess_of_Power_episodes)
seasons = {1: dict(start=1, end=13, color='#A6214E'),
           2: dict(start=14, end=20, color='#A6214E'),
           3: dict(start=21, end=26, color='#A6214E')}

# Episodes that logically 'follow' each other directly in the plot
plot_threads = [
    (1, 2, r'''Adora alone'''),
    (2, 3, r'''Adora alone'''),
    (3, 4, r'''Recruiting Perfuma'''),
    (3, 5, r'''Recruiting Mermista'''),
    (3, 6, r'''Recruiting Entrapta'''),
    (3, 8, r'''Recruting Frosta'''),
    (8, 9, r'''Glimmer rescue mission'''),
    (9, 10, r'''Glimmer's injury'''),
    (9, 10, r'''Entrapta in Fright Zone'''),
    (10, 11, r'''Healing Glimmer'''),
    (10, 11, r'''Finding First Ones' tech'''),
    (11, 12, r'''Adora/Light Hope'''),
    (11, 12, r'''Stolen First Ones' tech'''),
    (12, 13, r'''Hacked planet'''),
    (10, 14, r'''Entrapta and the Horde'''),
    (14, 15, r'''Entrapta rescue mission'''),
    (6, 18, r'''Virus First Ones' tech'''),
    (7, 19, r'''Shadow Weaver's past'''),
    (16, 20, r'''Mysterious Signal'''),
    (19, 20, r'''Shadow Weaver's escape'''),
    (19, 21, r'''Shadow Weaver's escape'''),
    (20, 21, r'''Catra's punishment'''),
    (20, 21, r'''Mysterious Signal'''),
    (16, 22, r'''The Portal Machine'''),
    (21, 22, r'''Crimson Waste arc'''),
    (22, 23, r'''Crimson Waste arc'''),
    (22, 24, r'''The Portal Machine'''),
    (23, 24, r'''Adora captured'''),
    (24, 25, r'''The Portal'''),
    (25, 26, r'''The Portal''')
]

# Episodes that foreshadow a future episode
foreshadowing = [
]

# Episodes that callback to a detail of a previous episode
# Reoccurences of the subject of a callback are ignored
callbacks = [
]
