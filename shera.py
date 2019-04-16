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
    13: 'The Battle of Bright Moon'
}

num_episodes = len(episodes)

# Season colors also set to match Wikipedia
# (Section colors from https://en.wikipedia.org/wiki/List_of_She-Ra:_Princess_of_Power_episodes)
seasons = {1: dict(start=1, end=13, color='#A6214E')}

# Episodes that logically 'follow' each other directly in the plot
plot_threads = [
    (1, 2, r'''Adora alone'''),
    (2, 3, r'''Adora alone'''),
    (3, 4, r'''Recruiting other princesses'''),
    (3, 5, r'''Recruiting other princesses'''),
    (3, 6, r'''Recruiting other princesses'''),
    (3, 8, r'''Adora / Cat-Ra'''),
    (8, 9, r'''Rescue mission'''),
    (9, 10, r'''Glimmer's injury / Entrapta in Fright Zone'''),
    (10, 11, r'''First One's tech / healing'''),
    (11, 12, r'''Stolen first one's tech'''),
    (12, 13, r'''Hacked planet''')
]

foreshadowing = [
    (1, 2, r'''Insert foreshadowing; thing foreshadowed''')
]

callbacks = [
    (2, 1, r'''blah''')
]
