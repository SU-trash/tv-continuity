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
    30: "Northwest Mansion Mystery", # "Northwest Mansion Noir" ?
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
    (4, 11, r'''Gideon arc'''),
    (11, 19, r'''Gideon arc'''),
    (1, 20, r'''Stan / Vending machine door'''),
    (19, 20, r'''Gideon arc'''),
    (9, 28, r'''Blendin's revenge'''),
    (20, 31, r'''Portal machine arc'''),
    (22, 24, r'''Bunker laptop'''),
    (31, 35, r'''Dimensional rift'''),
    (35, 37, r'''Dimensional rift'''),
    (37, 38, r'''Weirdmageddon arc'''),
    (38, 39, r'''Weirdmageddon arc'''),
    (39, 40, r'''Weirdmageddon arc'''),
]

# Episodes that foreshadow a future episode
foreshadowing = [
    (1, 9, r'''Blendin appears briefly in background'''),
    (1, 19, r'''Bill references throughout Shack; Bill's existence'''),
    (1, 35, r'''Bill references throughout M. Shack; Ford's involvement with Bill'''),
    (1, 31, r'''Intro theme cryptogram: "STAN IS NOT WHAT HE SEEMS"; The two Stans'''),
    (1, 31, r'''Shack totem pole depicts Kolus (imitator brother of Thunderbird); The two Stans'''),
    (1, 40, r'''Zodiac wheel on intro cipher page'''),
    (2, 4, r'''Gideon in ad on back of magazine'''),
    (2, 8, r'''"You call that Ben Franklin? He looks like a woman!"'''),
    (2, 9, r'''Blendin appears briefly in background'''),
    (2, 31, r'''STNLYMBL ('Stanley-mobile') license plate instead of 'Stanford-mobile'; The two Stans'''),
    (3, 9, r'''Blendin appears briefly in background'''),
    (3, 31, r'''Stan's strong reactions to the wax figure of himself; The two Stans'''),
    (5, 20, r'''Hallucinated dog seems to say "must distrust Grunkle" backwards; Stan's portal machine'''),
    (6, 15, r'''Mer-people's existence mentioned'''),
    (8, 9, r'''Time Baby mentioned in secret document'''),
    (8, 27, r'''Serial number on -$12 bill deciphers to 'BLIND'; Society of the Blind Eye'''),
    (9, 10, r'''Arcade shows briefly in 'camouflage' setting of Blendin's suit'''),
    (9, 18, r'''Sap-dinosaurs show briefly in 'camouflage' setting of Blendin's suit'''),
    (9, 31, r'''Ford in past Mystery Shack; The two Stans'''),
    (11, 20, r'''"[The M. Shack] holds a secret you couldn't possibly imagine."; Journal 1 hidden in M. Shack'''),
    (14, 32, r'''"I regularly commit massive tax fraud."; Stan assuming Ford's identity'''),
    (16, 31, r'''Spare room, glasses/Stan's reaction to them; The two Stans'''),
    (17, 37, r'''"the apocalypse is coming soon"; Weirdmageddon'''),
    (19, 31, r'''Pair of swings in Stan's memory, one broken; The two Stans'''),
    (19, 31, r'''Ford in background of wrestling memory; The two Stans'''),
    (20, 32, r'''Rainbow prism reflection in Author flashback; Author lived in M. Shack'''),
    (22, 30, r'''Threatened "last form you'll ever take" matches Dipper's pose when turned to wood'''),
    (22, 31, r'''"That six-fingered nerd hasn't been the same in 30 years"; The two Stans'''),
    (24, 31, r'''"who would sacrifice everything they'd worked for just for their dumb sibling?"; The two Stans'''),
    (26, 32, r'''Parallel - genius choosing whether to abandon their dreams to stay with their family; The Stans' schism'''),
    (32, 35, r'''Ford checking Stan's eyes; Ford's involvement with Bill'''),
    (35, 40, r'''Dipper tries to memory erase Ford when he thinks he's possessed; Bill defeated via same method''')
]

# Episodes that callback to a detail of a previous episode
# Reoccurences of the subject of a callback are ignored
callbacks = [
    (4, 3, r'''Detached S on M. Shack'''),
    (4, 3, r'''Mabel wears llama sweater as suggested by wax figure'''),
    (6, 3, r'''Picture of Dipper and wax figure in Mabel's scrapbook'''),
    (9, 1, r'''Passed through while time-travelling'''),
    (9, 2, r'''Passed through while time-travelling'''),
    (9, 3, r'''Passed through while time-travelling'''),
    (9, 8, r'''Pioneer exclaims "By Trembley!"'''),
    (10, 5, r'''Water tower graffiti'''),
    (11, 4, r'''Missing painting Stan stole'''),
    (12, 5, r'''90s teenagers who caused last ghost incident'''),
    (14, 8, r'''Deputy Durland being unable to read'''),
    (14, 12, r'''Stan parking in handicapped spaces'''),
    (14, 13, r'''Stan's fez changed after losing old one'''),
    (14, 13, r'''The Shred Pal'''),
    (19, 2, r'''Mabel's giant hamster ball'''),
    (19, 2, r'''Xyler and Craz from Mabel's imagination'''),
    (22, 5, r'''Dipper/Wendy's zip-lips-throw-away-key gesture'''),
    (32, 2, r"'Stan o War'"),
    (33, 31, r'''Ducktective twin brother plot twist'''),
    (39, 3, r'''Waffles with arms as drawn by Mabel'''),
    (40, 7, r'''Clone dippers in credits photo''')
]
