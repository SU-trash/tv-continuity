#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Data on the show Steven Universe.'''

title = 'Steven Universe'

# Season colors also set to match Wikipedia
# (Section colors from https://en.wikipedia.org/wiki/List_of_Steven_Universe_episodes)
seasons = {1: dict(start=1, end=52, color='#FF5E6D'),
           2: dict(start=53, end=78, color='#91ECDD'),
           3: dict(start=79, end=103, color='#B895D1'),
           4: dict(start=104, end=128, color='#A12766'),
           5: dict(start=129, end=160, color='#ACDF7D')}

# Dict of episode numbers and titles. Double-length episodes are instead indexed with a string
# containing the episode numbers they take up, separated by a forward slash (/), or with a
# dash for > 2-part episodes. This number or string will appear in the node hovertext.
# Dicts are now conveniently ordered as of python 3.7 papa bless
episodes = {
    1: 'Gem Glow',
    2: 'Laser Light Cannon',
    3: 'Cheeseburger Backpack',
    4: 'Together Breakfast',
    5: 'Frybo',
    6: 'Cat Fingers',
    7: 'Bubble Buddies',
    8: 'Serious Steven',
    9: 'Tiger Millionaire',
    10: "Steven's Lion",
    11: 'Arcade Mania',
    12: 'Giant Woman',
    13: 'So Many Birthdays',
    14: 'Lars and the Cool Kids',
    15: 'Onion Trade',
    16: 'Steven the Sword Fighter',
    17: 'Lion 2: The Movie',
    18: 'Beach Party',
    19: "Rose's Room",
    20: 'Coach Steven',
    21: 'Joking Victim',
    22: 'Steven and the Stevens',
    23: 'Monster Buddies',
    24: 'An Indirect Kiss',
    25: 'Mirror Gem',
    26: 'Ocean Gem',
    27: 'House Guest',
    28: 'Space Race',
    29: 'Secret Team',
    30: 'Island Adventure',
    31: 'Keep Beach City Weird',
    32: 'Fusion Cuisine',
    33: "Garnet's Universe",
    34: 'Watermelon Steven',
    35: 'Lion 3: Straight to Video',
    36: 'Warp Tour',
    37: 'Alone Together',
    38: 'The Test',
    39: 'Future Vision',
    40: 'On the Run',
    41: 'Horror Club',
    42: 'Winter Forecast',
    43: 'Maximum Capacity',
    44: 'Marble Madness',
    45: "Rose's Scabbard",
    46: 'Open Book',
    47: 'Shirt Club',
    48: 'Story for Steven',
    49: 'The Message',
    50: 'Political Power',
    51: 'The Return',
    52: 'Jail Break',
    53: 'Full Disclosure',
    54: 'Joy Ride',
    55: 'Say Uncle',
    56: 'Love Letters',
    57: 'Reformed',
    58: 'Sworn to the Sword',
    59: 'Rising Tides, Crashing Skies',
    60: 'Keeping It Together',
    61: 'We Need to Talk',
    62: 'Chille Tid',
    63: 'Cry for Help',
    64: 'Keystone Motel',
    65: 'Onion Friend',
    66: 'Historical Friction',
    67: 'Friend Ship',
    68: 'Nightmare Hospital',
    69: "Sadie's Song",
    70: 'Catch and Release',
    71: 'When It Rains',
    72: 'Back to the Barn',
    73: 'Too Far',
    74: 'The Answer',
    75: "Steven's Birthday",
    76: "It Could've Been Great",
    77: 'Message Received',
    78: 'Log Date 7 15 2',
    79: 'Super Watermelon Island',
    80: 'Gem Drill',
    81: 'Same Old World',
    82: 'Barn Mates',
    83: 'Hit the Diamond',
    84: 'Steven Floats',
    85: 'Drop Beat Dad',
    86: 'Mr. Greg',
    87: 'Too Short to Ride',
    88: 'The New Lars',
    89: 'Beach City Drift',
    90: 'Restaurant Wars',
    91: "Kiki's Pizza Delivery Service",
    92: 'Monster Reunion',
    93: 'Alone at Sea',
    94: 'Greg the Babysitter',
    95: 'Gem Hunt',
    96: 'Crack the Whip',
    97: 'Steven vs. Amethyst',
    '98/99': 'Bismuth',
    100: 'Beta',
    101: 'Earthlings',
    102: 'Back to the Moon',
    103: 'Bubbled',
    104: 'Kindergarten Kid',
    105: 'Know Your Fusion',
    106: "Buddy's Book",
    107: 'Mindful Education',
    108: 'Future Boy Zoltron',
    109: 'Last One Out of Beach City',
    110: 'Onion Gang',
    '111/112': 'Gem Harvest',
    113: 'Three Gems and a Baby',
    114: "Steven's Dream",
    115: 'Adventures in Light Distortion',
    116: 'Gem Heist',
    117: 'The Zoo',
    118: 'That Will Be All',
    119: 'The New Crystal Gems',
    120: 'Storm in the Room',
    121: 'Rocknaldo',
    122: 'Tiger Philanthropist',
    123: 'Room for Ruby',
    124: 'Lion 4: Alternate Ending',
    125: 'Doug Out',
    126: 'The Good Lars',
    127: 'Are You My Dad?',
    128: 'I Am My Mom',
    129: 'Stuck Together',
    130: 'The Trial',
    131: 'Off Colors',
    132: "Lars' Head",
    133: 'Dewey Wins',
    134: 'Gemcation',
    135: 'Raising the Barn',
    136: 'Back to the Kindergarten',
    137: 'Sadie Killer',
    138: 'Kevin Party',
    139: 'Lars of the Stars',
    140: 'Jungle Moon',
    141: 'Your Mother and Mine',
    142: 'The Big Show',
    143: 'Pool Hopping',
    144: 'Letters to Lars',
    145: "Can't Go Back",
    146: 'A Single Pale Rose',
    147: "Now We're Only Falling Apart",
    148: "What's Your Problem",
    149: 'The Question',
    150: 'Made of Honor',
    '151/152': 'Reunited',
    153: 'Legs From Here to Homeworld',
    154: 'Familiar',
    155: 'Together Alone',
    156: 'Escapism',
    '157-160': 'Change Your Mind'
}

# Episodes that logically 'follow' each other directly in the plot
plot_threads = [
    (1, 23, Plot.CAUSAL, r'''Centipeedle arc'''),
    (23, 92, Plot.CAUSAL, r'''Centipeedle arc'''),
    (92, 153, Plot.CAUSAL, r'''Centipeedle arc'''),
    (3, 38, Plot.CAUSAL, r'''Sea Spire test'''),
    (9, 122, Plot.CAUSAL, r'''Wrestling arc'''),
    (10, 17, Plot.CAUSAL, r'''Lion arc'''),
    (17, 35, Plot.CAUSAL, r'''Lion arc'''),
    (35, 45, Plot.CAUSAL, r'''Lion arc'''),
    (17, 45, Plot.CAUSAL, r'''Rose's Sword/Armory'''),
    (24, 26, Plot.REFERENTIAL, r'''Steven's healing power'''),
    (24, 27, Plot.REFERENTIAL, r'''Steven's healing power'''),
    (27, 92, Plot.CAUSAL, r'''Loss of Steven's healing power'''),
    (25, 26, Plot.SERIAL, r'''Lapis arc'''),
    (26, 49, Plot.CAUSAL, r'''Lapis arc'''),
    (26, 27, Plot.CAUSAL, r'''Greg's broken leg'''),
    (28, 36, Plot.CAUSAL, r'''Galaxy warp checking/sticker'''),
    (34, 79, Plot.CAUSAL, r'''Watermelon Stevens'''),
    (35, 124, Plot.CAUSAL, r'''Rose's tape for Steven'''),
    (35, 132, Plot.CAUSAL, r'''Mystery of Lion's nature'''),
    (36, 44, Plot.SERIAL, r'''Peridot arc'''),
    (37, 89, Plot.CAUSAL, r'''Kevin arc'''),
    (89, 138, Plot.REFERENTIAL, r'''Kevin/Steven'''),  # I'd say this isn't an arc, Kevin's just a plot device here
    (39, 42, Plot.CAUSAL, r'''Garnet's future vision'''),
    (44, 49, Plot.CAUSAL, r'''Homeworld gems invasion arc'''),
    (49, 50, Plot.CAUSAL, r'''Homeworld gems invasion arc'''),
    (49, 51, Plot.CAUSAL, r'''Homeworld gems invasion arc'''),
    (51, 52, Plot.SERIAL, r'''Homeworld gems invasion arc'''),
    (52, 53, Plot.CAUSAL, r'''Homeworld gems invasion arc'''),
    (52, 74, Plot.CAUSAL, r'''"We were waiting for your birthday"'''),
    (48, 61, Plot.CAUSAL, r'''Rose/Greg flashback arc'''),
    (61, 94, Plot.CAUSAL, r'''Rose/Greg flashback arc'''),  # 2
    (52, 62, Plot.CAUSAL, r'''Malachite arc'''),
    (62, 79, Plot.SERIAL, r'''Malachite arc'''),
    (52, 54, Plot.CAUSAL, r'''Peridot hunt arc'''),
    (54, 60, Plot.CAUSAL, r'''Peridot hunt arc'''),
    (60, 63, Plot.SERIAL, r'''Peridot hunt arc'''),
    (63, 67, Plot.SERIAL, r'''Peridot hunt arc'''),
    (67, 70, Plot.SERIAL, r'''Peridot hunt arc'''),
    (45, 68, Plot.REFERENTIAL, r'''Rose's Sword'''),
    (58, 68, Plot.CAUSAL, r'''Connie's training'''),
    (58, 95, Plot.CAUSAL, r'''Connie's training'''),
    (44, 60, Plot.CAUSAL, r'''Gem mutants experiment released by Peridot'''),
    (60, 68, Plot.CAUSAL, r'''Gem mutants'''),
    (63, 64, Plot.SERIAL, r'''Sardonyx arc'''),
    (64, 67, Plot.SERIAL, r'''Sardonyx arc'''),
    (52, 70, Plot.CAUSAL, r'''Cluster arc'''),  # This one's pretty much a Chekhov's Gun
    (70, 71, Plot.SERIAL, r'''Cluster arc'''),
    (60, 71, Plot.REFERENTIAL, r'''Gem Mutants'''),  # TODO: Should probably be same as Nightmare Hospital's level?
    (71, 72, Plot.CAUSAL, r'''Cluster arc'''),
    (72, 73, Plot.CAUSAL, r'''Cluster arc'''),
    (13, 75, Plot.CAUSAL, r'''Steven's age fluctuation arc'''),  # 2 Also 1 from Cat Fingers? Need better system for powers that enter the canon
    (72, 76, Plot.CAUSAL, r'''Cluster arc'''),
    (72, 77, Plot.REFERENTIAL, r'''Peridot's giant robot'''),  # The robot is more a plot device here than anything IMO
    (76, 77, Plot.SERIAL, r'''Peridot/Diamond communicator arc'''),
    (76, 79, Plot.CAUSAL, r'''Cluster arc'''),
    (79, 80, Plot.SERIAL, r'''Cluster arc'''),
    (60, 80, Plot.REFERENTIAL, r'''Gem Mutants'''),
    (79, 81, Plot.CAUSAL, r'''Lapis redemption arc'''),
    (81, 82, Plot.SERIAL, r'''Lapis/Peridot barn arc.'''),
    (82, 83, Plot.SERIAL, r'''Rubies arc'''),
    (48, 85, Plot.CAUSAL, r'''Greg/Marty's contract'''),
    (85, 86, Plot.CAUSAL, r'''Greg's fortune'''),
    (79, 93, Plot.CAUSAL, r'''Jasper/Lapis arc'''),
    (85, 93, Plot.CAUSAL, r'''Greg's fortune'''),
    (93, 95, Plot.CAUSAL, r'''Jasper arc'''),
    (95, 96, Plot.CAUSAL, r'''Jasper arc'''),
    (96, 97, Plot.CAUSAL, r'''Amethyst self-worth arc'''),
    (35, '98/99', Plot.CAUSAL, r'''Bismuth's gem'''),
    (96, 100, Plot.CAUSAL, r'''Jasper arc'''),
    (97, 100, Plot.CAUSAL, r'''Amethyst self-worth arc'''),
    (100, 101, Plot.SERIAL, r'''Jasper arc'''),
    (83, 102, Plot.CAUSAL, r'''Rubies arc'''),
    (101, 102, Plot.SERIAL, r'''Rubies arrival, RQ killed PD arc'''),
    (102, 103, Plot.SERIAL, r'''Rubies arc'''),
    (101, 105, Plot.CAUSAL, r'''Smoky Quartz arc'''),
    (114, 115, Plot.SERIAL, r'''Zoo arc'''),
    (115, 116, Plot.SERIAL, r'''Zoo arc'''),
    (116, 117, Plot.SERIAL, r'''Zoo arc'''),
    (117, 118, Plot.SERIAL, r'''Zoo arc'''),
    (115, 119, Plot.CAUSAL, r'''Crystal Gems' absence'''),
    (103, 123, Plot.CAUSAL, r'''Rubies arc - Navy'''),
    (44, 125, Plot.CAUSAL, r'''List of humans Steven gave Peridot'''),
    (118, 125, Plot.CAUSAL, r'''BD wanting to save some humans'''),
    (125, 126, Plot.CAUSAL, r'''Disappearing townies arc'''),  # Causal but episode focus isn't on disappearances
    (126, 127, Plot.SERIAL, r'''Disappearing townies arc'''),
    (127, 128, Plot.SERIAL, r'''Disappearing townies arc'''),
    (128, 129, Plot.SERIAL, r'''Steven/Lars on Homeworld arc'''),
    ('98/99', 130, Plot.CAUSAL, r'''Steven assuming Rose used Breaking Point'''),
    (102, 130, Plot.CAUSAL, r'''RQ killed PD arc + Eyeball'''),
    (129, 130, Plot.SERIAL, r'''Steven/Lars on Homeworld arc'''),
    (130, 131, Plot.SERIAL, r'''Steven/Lars on Homeworld arc'''),
    (131, 132, Plot.SERIAL, r'''Steven/Lars on Homeworld arc'''),
    (128, 133, Plot.CAUSAL, r'''Townies' concern with handling of gem events'''),
    (128, 133, Plot.CAUSAL, r'''Steven/Connie fight arc'''),
    (133, 134, Plot.SERIAL, r'''Steven/Connie fight arc'''),
    (130, 135, Plot.CAUSAL, r'''Lapis leaving arc'''),
    (135, 136, Plot.CAUSAL, r'''Lapis leaving arc - Peridot'''),
    (134, 138, Plot.SERIAL, r'''Steven/Connie fight arc'''),
    (132, 139, Plot.CAUSAL, r'''Lars/Off Colors arc'''),
    (139, 140, Plot.SERIAL, r'''Stranded arc'''),
    (137, 142, Plot.CAUSAL, r'''Sadie Killer arc'''),
    (133, 144, Plot.CAUSAL, r'''Non-Mayor Dewey arc / Beach City preparation for gem events'''),
    (137, 144, Plot.CAUSAL, r'''New Big Donut employee needed'''),
    (135, 145, Plot.CAUSAL, r'''Lapis leaving arc'''),
    (144, 145, Plot.CAUSAL, r'''Ronaldo's lookout duty'''),
    (134, 146, Plot.CAUSAL, r'''Pearl's unspeakable secret arc'''),
    (145, 146, Plot.CAUSAL, r'''Memory/Vision of Pearl'''),
    (146, 147, Plot.CAUSAL, r'''RQ=PD aftermath arc - Sapphire'''),
    (146, 148, Plot.CAUSAL, r'''RQ=PD aftermath arc - Amethyst'''),
    (146, 149, Plot.CAUSAL, r'''RQ=PD aftermath arc - Ruby'''),
    ('98/99', 150, Plot.CAUSAL, r'''Bismuth arc'''),
    (149, 150, Plot.SERIAL, r'''Ruby/Sapphire wedding arc'''),
    (80, '151/152', Plot.CAUSAL, r'''Steven's friendship with the Cluster'''),
    (145, '151/152', Plot.CAUSAL, r'''Lapis leaving arc'''),
    (150, '151/152', Plot.SERIAL, r'''Ruby/Sapphire wedding arc'''),
    (124, 153, Plot.CAUSAL, r'''Pink's ship'''),
    ('151/152', 153, Plot.SERIAL, r'''Diamonds/Steven arc'''),
    (153, 154, Plot.SERIAL, r'''Diamonds/Steven Homeworld arc'''),
    (154, 155, Plot.SERIAL, r'''Diamonds/Steven Homeworld arc'''),
    (155, 156, Plot.SERIAL, r'''Diamonds/Steven Homeworld arc'''),
    (156, '157-160', Plot.SERIAL, r'''Diamonds/Steven Homeworld arc''')
]

# Episodes that foreshadow a future episode
foreshadowing = [
    (1, 52, Foreshadowing.MAJOR, r'''Two shooting stars in OP when Garnet appears; Garnet fusion'''),
    (1, 12, Foreshadowing.MAJOR, r'''Temple statue; Existence of fusion'''),
    (1, 26, Foreshadowing.MAJOR, r'''Monsters have gems; Monsters are corrupted gems'''),
    (1, 7, Foreshadowing.MINOR, r'''Bracelet in freezer; setting up for Connie intro'''),
    (1, 52, Foreshadowing.MAJOR, r'''Garnet having two gems; Garnet fusion'''),
    (1, 26, Foreshadowing.MAJOR, r'''Cookie cat song: "came to this planet from outer space"; Gems are aliens'''),
    (1, 146, Foreshadowing.MAJOR, r'''Cookie cat song: "pet for your tummy", "left his family behind"; RQ=PD'''),
    (1, 26, Foreshadowing.MAJOR, r'''Pearl: "Properties of this planet"; Gems are aliens'''),
    (2, 39, Foreshadowing.MAJOR, r'''Garnet adjusts glasses then announces only way to destroy Red Eye; Future vision'''),
    (2, 17, Foreshadowing.MINOR, r'''"You've gotta know where it is... Like a cave dungeon"; Rose's armory'''),
    (2, 16, Foreshadowing.MINOR, r'''"...or a cloud fortress"; Sky Arena'''),
    (3, 13, Foreshadowing.MINOR, r'''"You should have seen it in its heyday"; Gems' age'''),
    (3, 26, Foreshadowing.MAJOR, r'''"Oasis for gems on earth"; Gems are aliens'''),
    (3, 39, Foreshadowing.MAJOR, r'''Garnet senses danger several times while adjusting glasses; Future vision'''),
    (4, 19, Foreshadowing.MAJOR, r'''Glimpse of Rose's Room'''),
    (4, 52, Foreshadowing.MAJOR, r'''Garnet has two door lights; Garnet fusion'''),
    (6, 9, Foreshadowing.MINOR, r'''Amethyst shapeshifts briefly into Purple Puma'''),
    (7, 157, Foreshadowing.MINOR, r'''Temple statue (Obsidian)'s sword visible in ocean'''),  # Repeat from 26 not counted
    (8, 40, Foreshadowing.MAJOR, r'''"This was once a gem battlefield"; Gem rebellion'''),
    (8, 76, Foreshadowing.MAJOR, r'''Rose vs diamonds mural; Existence of diamond authority'''),
    (9, 146, Foreshadowing.MAJOR, r'''"that's why we're all here... to be wild and free... and make up nicknames"; RQ=PD'''),
    (10, 35, Foreshadowing.MAJOR, r'''Lion is pink; Lion belonging to Rose'''),
    (10, 146, Foreshadowing.MAJOR, r'''Pet lion; royalty symbolism; RQ=PD'''),
    (10, 40, Foreshadowing.MAJOR, r'''"We kept Amethyst"; Amethyst's origin'''),
    (11, 39, Foreshadowing.MAJOR, r'''"Heightened senses", third eye symbolism; Future vision'''),
    (11, 51, Foreshadowing.MINOR, r'''"fighting a giant foot"; homeworld invasion hand ship'''),
    (11, 52, Foreshadowing.MAJOR, r'''Garnet's third eye; Garnet fusion'''),
    (13, 16, Foreshadowing.MAJOR, r'''"even if your [...] body's an illusion"; Gems' bodies being light constructs'''),
    (13, 146, Foreshadowing.MAJOR, r'''Crown/cape; royalty symbolism; RQ=PD'''),
    (14, 17, Foreshadowing.MINOR, r'''Dogcopter 3 poster in background'''),
    (16, 26, Foreshadowing.MAJOR, r'''Gems poof same as monsters; Monsters are corrupted gems'''),
    (16, 39, Foreshadowing.MAJOR, r'''Garnet anticipates Steven raising his hand; Future vision'''),
    (16, 146, Foreshadowing.MAJOR, r'''Diamond on Holo-Pearl's chest; Pearl belonged to PD'''),
    (17, 132, Foreshadowing.MAJOR, r'''Lion can walk on water like Jesus; Lion was resurrected'''),
    (17, 146, Foreshadowing.MAJOR, r'''Giant penny; batman; secret identity; RQ=PD'''),
    (19, 35, Foreshadowing.MINOR, r'''Tiny Floating Pink Whale has Rose's voice'''),
    (22, 26, Foreshadowing.MAJOR, r'''Flashforward of ocean disappearance'''),
    (22, 52, Foreshadowing.MAJOR, r'''Garnet playing keytar ('fusion' instrument); Garnet fusion'''),
    (23, 26, Foreshadowing.MAJOR, r'''Centipeedle humanoid stage while reforming; Monsters are corrupted gems'''),
    (23, 52, Foreshadowing.MAJOR, r'''"Shut down by the G-squad"; Garnet fusion'''),
    (28, 146, Foreshadowing.MAJOR, r'''Pink diamond on Pearl's spacesuit; Pearl belonged to PD'''),
    (31, 76, Foreshadowing.MAJOR, r'''"They're here to hollow out the earth"; Gem plans for Earth'''),
    (31, 76, Foreshadowing.MAJOR, r'''"It's all part of the great diamond authority"; Existence of Diamond Authority'''),
    (31, 140, Foreshadowing.MAJOR, r'''Upside down diamond on currency; Pink Diamond's design'''),
    (31, 146, Foreshadowing.MAJOR, r"Pearl's aversion to shape-shifting; Pearl's role in PD's 'shattering'"),
    (32, 52, Foreshadowing.MAJOR, r'''Ruby/Sapphire outlines briefly visible while Alexandrite unfusing; Garnet fusion'''),
    (33, 52, Foreshadowing.MAJOR, r'''"He's not ready to learn that I have secret animal friends"; Garnet fusion'''),
    (34, 146, Foreshadowing.MAJOR, r'''Watermelon crown; royalty symbolism; RQ=PD'''),
    (36, 40, Foreshadowing.MAJOR, r'''"They're coming back! I can't do this, not again!"; Gem rebellion'''),
    (36, 40, Foreshadowing.MAJOR, r'''"Preparing to locate and manually reactivate Kindergar-"; Kindergarten(s)'''),
    (37, 52, Foreshadowing.MAJOR, r'''"Fusion is really hard, even for us." "Not for me"; Garnet fusion'''),
    (39, 40, Foreshadowing.MAJOR, r'''"Cookie Cat! [...] I never considered that you would be evil!"; Gems hurt the planet'''),
    (43, 51, Foreshadowing.MAJOR, r'''Jasper appears on totem pole in U-Stor; Jasper'''),
    (43, 82, Foreshadowing.MAJOR, r'''"Season 3... that's when the uptight neighbors the Richingtons move next-door"; Peridot/Lapis moving into barn'''),
    (44, '111/112', Foreshadowing.MINOR, r'''"I swear that's not his real name."; Steven/Greg's family name'''),
    (44, 153, Foreshadowing.MAJOR, r'''"But the records say that gems were wiped out on Earth"; Corrupting light was intended to destroy all Earth gems'''),
    (44, 155, Foreshadowing.MAJOR, r'''The Unfamiliar Familiar book; PD's new Pearl (unfamiliar 'familiar')'''),
    (45, 84, Foreshadowing.MAJOR, r'''Steven floats cartoonishly; Steven's floating power'''),
    (45, 146, Foreshadowing.MAJOR, r'''"If we win, we can never go home"; Rose not an earth Quartz; RQ=PD'''),
    (45, 72, Foreshadowing.MAJOR, r'''"My Pearl"; Pearls as servants'''),
    (45, 146, Foreshadowing.MAJOR, r'''"My Pearl"; Pearl belonged to Rose'''),
    (46, 153, Foreshadowing.MAJOR, r'''Clone Connie matches White Pearl's design'''),
    (48, 65, Foreshadowing.MINOR, r'''Vidalia's onion-themed name; Vidalia is Onion's mother'''),
    (51, 52, Foreshadowing.MAJOR, r'''"this shameless display" - Jasper, of Garnet; Garnet fusion'''),
    (51, 73, Foreshadowing.MAJOR, r'''"a puny overcooked runt" - Jasper, of Amethyst; Amethyst defective'''),
    (52, 76, Foreshadowing.MAJOR, r'''Diamond authority floor symbol; Existence of diamond authority'''),
    (58, 76, Foreshadowing.MAJOR, r'''Diamond authority symbol in arena; Existence of diamond authority'''),
    (58, 102, Foreshadowing.MAJOR, r'''Cracked PD symbol; death of PD'''),
    (59, 115, Foreshadowing.MAJOR, r'''Human zoo mentioned by ronaldo'''),
    (63, 146, Foreshadowing.MAJOR, r'''Pink diamond on Sardonyx's feet; Pearl belonged to PD'''),
    (67, 72, Foreshadowing.MAJOR, r'''"I'm just a Pearl"; Pearls as servants'''),
    (69, 114, Foreshadowing.MAJOR, r'''"I can't help it if I make a scene / stepping out of my hot pink limousine"; PD/palanquin'''),
    (70, 108, Foreshadowing.MINOR, r'''Happy Bear/Sad Bunny; Mr. Smiley/Mr. Frowney'''),
    (72, 74, Foreshadowing.MINOR, r'''"Welcome to Earth"'''),
    (72, 146, Foreshadowing.MAJOR, r'''"she looks like a fancy one"; Pearl belonged to PD"'''),
    (76, 140, Foreshadowing.MAJOR, r'''Moon base diamond throne is small; PD design'''),
    (76, 146, Foreshadowing.MAJOR, r'''PD symbols in Lion's warp; RQ=PD'''),
    (76, 146, Foreshadowing.MAJOR, r'''"We are literally walking in the footsteps of the diamonds."; RQ=PD'''),
    #(76, ???, Foreshadowing.MAJOR, r'''WD's gem being on her forehead; Pearl used to be WD's pearl'''),
    (81, 86, Foreshadowing.MINOR, r'''Pepe's Burgers ad in background'''),
    (81, 92, Foreshadowing.MAJOR, r'''Yellow/blue/white-tinged nova shown in flashback; Source of corruption'''),
    (81, '98/99', Foreshadowing.MAJOR, r'''Bismuth briefly appears in flashback; Bismuth's identity'''),
    (84, 146, Foreshadowing.MAJOR, r'''Steven's skull appears on a pink diamond-shaped pillow; RQ=PD'''),
    (86, 118, Foreshadowing.MAJOR, r'''Greg/Pearl yellow/blue symbolism; YD/BD mourning PD'''),
    (94, 131, Foreshadowing.MAJOR, r'''"you better pray your space goddess' magic can bring people back from the dead"'''),
    ('98/99', 146, Foreshadowing.MAJOR, r'''Rose's sword couldn't shatter gems; PD still alive'''),
    ('98/99', 153, Foreshadowing.MINOR, r'''Bismuth mentions defeating a Nephrite from a drop-ship; Nephrite's name'''),
    (100, 118, Foreshadowing.MINOR, r'''Carnelian and Skinny's exit holes described'''),
    (102, 134, Foreshadowing.MAJOR, r'''Pearl covering her mouth when details of PD's death are brought up'''),
    (102, 146, Foreshadowing.MAJOR, r"Eyeball claims to have witnessed RQ murder PD while currently being fooled by shapeshifting; Pearl's role in PD's 'shattering'"),
    (103, 146, Foreshadowing.MAJOR, r'''"That's more of a pinkish-red than a real Rose Quartz reddish-pink."; RQ=PD'''),
    (106, 114, Foreshadowing.MAJOR, r'''PD's palanquin appears in journal'''),
    (106, 132, Foreshadowing.MAJOR, r'''A non-magical lion with the same nose as Lion is seen in the flashback; Lion's origin'''),
    (110, 146, Foreshadowing.MAJOR, r'''Garbanzo fakes his own death; PD faking her death'''),
    (113, 146, Foreshadowing.MAJOR, r'''Baby Steven's clothes make diamond shape around his gem; RQ=PD'''),
    (115, 146, Foreshadowing.MAJOR, r'''"When I still served... Homeworld"; Pearl unwilling to reveal the gem she served; Pearl belonged to PD'''),
    (120, '151/152', Foreshadowing.MINOR, r'''Lonely Arms video game image looks like Cluster/YD's ship arm wresting'''),
    (124, 146, Foreshadowing.MAJOR, r'''Pink's ship in desert where Rose stores her stuff; RQ=PD'''),
    (130, 146, Foreshadowing.MAJOR, r'''"Someone with supreme authority"; RQ=PD'''),
    (140, 146, Foreshadowing.MAJOR, r'''Steven has PD's memories; RQ=PD'''),
    (141, 146, Foreshadowing.MAJOR, r'''"Rose Quartz isn't real"; RQ=PD'''),
    (148, 149, Foreshadowing.MINOR, r'''"Why would she be a cowboy?!"'''),
    (145, '151/152', Foreshadowing.MINOR, r'''"You could drop the barn on the beach"'''),
    (153, 155, Foreshadowing.MAJOR, r'''Gem on stomach; White Pearl originally belonged to PD''')
    #(154, ???, r'''Diamond secretions collected / Steven creating pebble; Diamond secretions used in injectors to create life''') # TODO when relevant
    #(156, ???, r'''War between CGs and homeworld, resolution?'''),
]

# Episodes that callback to a detail of a previous episode
# Reoccurences of the subject of a callback are ignored (e.g. the Crying Breakfast Friends cartoon
# appears many times throughout the show but is only recorded as a callback the first time it is
# reused)
callbacks = [
    (10, 6, r'''Cat fingers pic on Ronaldo's blog'''),
    (13, 1, r'''Lion Lickers freezer, Cookie Cat in Amethyst's junk'''),
    (15, 11, r'''Moped Onion won at arcade'''),
    (19, 2, r'''Greg's golf clubs'''),
    (19, 5, r'''Frybo'''),
    (19, 7, r'''"He was incredible" flashback'''),
    (21, 9, r'''Tiger Millionaire/Purple Puma poster in Big Donut break room'''),
    (22, 1, r'''Passed through while time-travelling'''),
    (22, 19, r'''Passed through while time-travelling'''),
    (25, 3, r'''Variation on Lapis' theme was heard in Sea spire'''),
    (26, 2, r'''"What's that thing you always say about the pork chops and the hotdogs?"'''),
    (26, 9, r'''Amethyst transforms into Purple Puma'''),
    (26, 16, r'''"I hate fighting me"'''),
    (28, 1, r'''Crying Breakfast Friends cartoon'''),
    (31, 2, r'''Pieces of red eye'''),
    (31, 11, r'''Drill monster holes'''),
    (31, 14, r'''Magic moss flowers'''),
    (34, 30, r'''Sadie's scar'''),
    (35, 14, r'''Steven/Lars' high five.'''),
    (35, 17, r'''Dogcopter'''),
    (35, 21, r'''VCR in Big Donut'''),
    (36, 12, r'''Steven Jr'''),
    (38, 8, r'''Trials resemble those in pyramid temple'''),
    (38, 36, r'''Ceiling hole from robonoid'''),
    (39, 25, r'''M.C. Bear Bear (new doll after Pearl stabbed old one)'''),
    (42, 23, r'''Shooting Star'''),
    (42, 32, r'''Steven having been grounded from TV'''),
    (43, 2, r'''Broken picture frame'''),
    (44, 2, r'''Peridot mentions Red Eye'''),
    (44, 7, r'''"Funky flow"'''),
    (46, 19, r'''Rose's Room, Tiny Floating Pink Whale'''),
    (46, 44, r'''Spirit Morph Saga book series'''),
    (47, 2, r'''T-shirt cannon'''),
    (49, 19, r'''Wailing Stone'''),
    (49, 26, '''The album cover Greg mentioned having a great idea for'''),
    (50, 45, r'''Quartizine trio'''),
    (51, 2, r'''Gems' telescope'''),
    (55, 39, r'''Wasps from Steven's imagination reappear'''),
    (55, 33, r'''Hopper appears in video game'''),
    (56, 12, r'''Garnet's swimming goggles'''),
    (57, 18, r'''Fashion magazine'''),
    (57, 25, r'''CPR dummy'''),
    (57, 40, r'''No Home Boys book'''),
    (58, 16, r'''Gem runes in backgrounds'''),
    (58, 28, r'''Carvings on wall match Galaxy Warp layout'''),
    (59, 10, r'''"Steven's Pregnant?!" joke referenced'''),
    (60, 57, r'''Note on fridge referencing Amethyst's consumption of engine oil'''),
    (60, 44, r'''Steven imitates robonoids' walking sound.'''),
    (64, 6, r'''"I don't like those brushes, they feel weird on your fur."'''),
    (66, 56, r'''"Humans aren't very good swimmers"; Jamie imitating Garnet's prior line'''),
    (70, 23, r'''Bubbled Chaaaaps'''),
    (70, 64, r'''"What's with you guys and making me pee outside!?"'''),
    (72, 28, r'''UUU Space Travel'''),
    (73, 70, r'''"Keep her outside on a leash?"'''),
    (74, 52, r''''Stronger than You' chords reprised in lullaby'''),
    (75, 2, r'''Song 'Let me Drive My Van into Your Heart' in background'''),
    (75, 13, r'''Steven's birthday suit'''),
    (75, 24, r'''Durian juice'''),
    (75, 61, r'''Connie/Greg "human beings" high five'''),
    (75, 68, r'''Connie no longer wearing fake glasses'''),
    (78, 70, r'''Peridot thinking a 'shirt' is any piece of clothing'''),
    (80, 78, r'''"Wow, thanks"'''),
    (81, 25, r'''Lapis/Steven blowing raspberries'''),
    (81, 28, r'''Caterpillar sleeping bag'''),
    (82, 78, r'''Camp Pining Hearts'''),
    (82, 80, r'''Drill hole reused to make pool'''),
    (83, 26, r'''"Bob"'''),
    (86, 16, r'''Sanic figurine'''),
    (86, 19, r'''Golf Quest Mini game'''),
    (86, 42, r'''Greg self-describes as "cherry man"'''),
    (86, 43, r'''Passions of Xanxor book'''),
    (86, 48, r''''Comet' theme reprised in Pepe's Burgers jingle'''),
    (87, 6, r'''Steven creating a cat finger'''),
    (89, 81, r'''Himitsu car company'''),
    (91, 10, r'''"Sorry for using the same pun twice"'''),
    (94, 43, r'''Li'l Butler'''),
    (94, 61, r'''The Philosophy Majors album'''),
    (95, 58, r''''Do It for Her' lyrics mentioned'''),
    (96, 60, r'''Pretty Hairstylist magazine'''),
    (96, 62, r'''"Bungacowa"'''),
    (96, 86, r'''Sadie humming Pepe's Burgers jingle'''),
    (97, 16, r'''"Boomerang shield"; Lonely Blade'''),
    ('98/99', 16, r'''Pearl having learnt that movies don't have to make sense'''),
    (100, 87, r'''Alien plush'''),
    (105, 74, r'''Garnet never asks questions; Rose's "No more questions"'''),
    (106, 56, r'''Jamie's "drama zone"'''),
    (107, 49, r'''"Hold the phone. Now give the phone to me"'''),
    (108, 8, r'''Steven's Funland ban'''),
    (109, 50, r'''The Ocean Town disaster'''),
    (113, 42, r'''Greg half-singing about his carabiner'''),
    (113, 49, r'''Greg: "I'm not that far away", to Steven'''),
    (113, 75, r'''"box made to look like it's wrapped"'''),
    (114, 48, r'''"Keep Out <i>Please</i>" sign'''),
    (114, 86, r'''Model sheets from Mr Greg shown in-show'''),
    (115, 103, r'''Navies seen floating in space'''),
    (119, 70, r'''Peridot trying to flush herself down the toilet'''),
    (119, 78, r'''Peridot mimicking Garnet's thumbs up'''),
    (120, 107, r'''Connie using mindful meditation'''),
    (122, 61, r''''mics are expensive' remark'''),
    (123, '111/112', r'''Inability to talk to corn'''),
    (124, 17, r'''Desert lizard, originally mentioned as "who knows where [Lion] got that.'''),
    (126, 14, r'''"It's all happening! Lars and the Cool Kids"; episode title'''),
    (126, 47, r'''Guitar Dad shirt'''),
    (126, 110, r'''Painting Vidalia was making of Yellowtail, completed on wall.'''),
    (127, 3, r''''Hey, Mr Postman' song'''),
    (128, 37, r'''"'Alone Together' song is Connie's ringtone'''),
    (133, 58, r''''How to Talk to People' book'''),
    (133, 22, r'''"Speech-a-Palooza"/Beach-a-Palooza'''),
    (134, 90, r'''Koala Princess dvds'''),
    (135, 34, r'''Onion wearing straw hat; "is that my hat?"'''),
    (135, 82, r'''"smaller than average lake"'''),
    (138, 75, r'''Pink shirt Connie gave Steven'''),
    (138, 109, r'''Sugar Shock Shutdown'''),
    (139, 37, r'''Stevonnie as "an experience"'''),
    (142, 109, r'''Mystery Girl cameos in background'''),
    (145, 25, r''''Mirror Gem' background music reprised when Lapis gets upset'''),
    (146, 6, r'''Gem sloop stored in Pearl's gem'''),
    (146, 56, r'''Sea Pals stored in Pearl's gem'''),
    (146, 97, r'''Pearl point stored in Pearl's gem'''),
    (146, 109, r'''Mystery Girl's # in Pearl's gem'''),
    (150, 11, r'''Meat Beat Mania game'''),
    ('151/152', 4, r'''Together Breakfast as wedding cake'''),
    ('151/152', 86, r'''Greg/Pearl/Steven's tailor-made suits'''),
    ('151/152', 113, r'''Razor Garnet gifted baby Steven'''),
    (156, 7, r'''Steven failing to convey something with a drawing, which is better explained in words''')
]

show = Show(title=title,
            seasons=seasons,
            episodes=episodes,
            plot_threads=plot_threads,
            foreshadowing=foreshadowing,
            callbacks=callbacks)