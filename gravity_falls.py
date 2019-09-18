#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''Data on the show Gravity Falls.'''

title = 'Gravity Falls'

episodes = {
    1: "Tourist Trapped",
    2: "The Legend of the Gobblewonker",
    3: "Headhunters",
    4: "The Hand That Rocks the Mabel",
    5: "The Inconveniencing",
    6: "Dipper vs. Manliness",
    7: "Double Dipper",
    8: "Irrational Treasure",
    9: "The Time Traveler's Pig",
    10: "Fight Fighters",
    11: "Little Dipper",
    12: "Summerween",
    13: "Boss Mabel",
    14: "Bottomless Pit!",
    15: "The Deep End",
    16: "Carpet Diem",
    17: "Boyz Crazy",
    18: "Land Before Swine",
    19: "Dreamscaperers",
    20: "Gideon Rises",
    21: "Scary-oke",
    22: "Into the Bunker",
    23: "The Golf War",
    24: "Sock Opera",
    25: "Soos and the Real Girl",
    26: "Little Gift Shop of Horrors",
    27: "Society of the Blind Eye",
    28: "Blendin's Game",
    29: "The Love God",
    30: "Northwest Mansion Mystery" "Northwest Mansion Noir",
    31: "Not What He Seems",
    32: "A Tale of Two Stans",
    33: "Dungeons, Dungeons & More Dungeons",
    34: "The Stanchurian Candidate",
    35: "The Last Mabelcorn",
    36: "Roadside Attraction",
    37: "Dipper and Mabel vs. the Future",
    38: "Weirdmageddon Part 1",
    39: "Weirdmageddon 2: Escape from Reality",
    40: "Weirdmageddon 3: Take Back The Falls"
}

# Season colors also set to match Wikipedia
# (Section colors from https://en.wikipedia.org/wiki/List_of_Gravity_Falls_episodes)
seasons = {1: dict(start=1, end=20, color='#19D39B'),
           2: dict(start=21, end=40, color='#49C9FF')}

# Episodes that logically 'follow' each other directly in the plot
plot_threads = [
    (1, 4, r'''Mystery of the Journals arc'''),
    (1, 31, r'''Stan / Vending machine mystery'''),
    (4, 11, r'''Gideon arc'''),
    (11, 19, r'''Gideon arc'''),
    (19, 20, r'''Gideon arc'''),
    (22, 24, r'''Bunker laptop'''),
]

# Episodes that foreshadow a future episode
foreshadowing = [
    (1, 31, r'''Intro theme cryptogram: "STAN IS NOT WHAT HE SEEMS"; The two Stans'''),
    (1, 9, r'''Blendin appears briefly in bushes.'''),
    (2, 31, r'''STNLYMBL ('Stanley-mobile') license plate instead of 'Stanford-mobile'; The two Stans'''),
    (3, 31, r'''Stan's strong reactions to the wax figure of himself; The two Stans'''),
    (9, 31, r'''Stanford Pines in past Mystery Shack; The two Stans'''),
    (16, 31, r'''Spare room, glasses/Stan's reaction to them; The two Stans'''),
    (19, 31, r'''Pair of swings in Stan's memory, one broken; The two Stans'''),
    (22, 31, r'''"That six-fingered nerd hasn't been the same in 30 years"; The two Stans'''),
    (24, 31, r'''"who would sacrifice everything they'd worked for just for their dumb sibling?"; The two Stans''')
]

# Episodes that callback to a detail of a previous episode
# Reoccurences of the subject of a callback are ignored
callbacks = [
    (22, 5, r'''Dipper/Wendy's zip-lips-throw-away-key gesture'''),
    (39, 3, r'''Waffles with arms as drawn by Mabel'''),
]