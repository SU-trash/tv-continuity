#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Star vs. the Forces of Evil.'''

# Parsed from https://en.wikipedia.org/wiki/List_of_Avatar:_The_Last_Airbender_episodes
show = Show(title='Avatar: The Last Airbender',
            brief_title='Avatar',
            seasons={1: dict(num_eps=20, color='#5599DF'),
                     2: dict(num_eps=20, color='#3FC351'),
                     3: dict(num_eps=21, color='#BE2808')},
            episodes={
                1: 'The Boy in the Iceberg',
                2: 'The Avatar Returns',
                3: 'The Southern Air Temple',
                4: 'The Warriors of Kyoshi',
                5: 'The King of Omashu',
                6: 'Imprisoned',
                '7/8': 'Winter Solstice',
                9: 'The Waterbending Scroll',
                10: 'Jet',
                11: 'The Great Divide',
                12: 'The Storm',
                13: 'The Blue Spirit',
                14: 'The Fortuneteller',
                15: 'Bato of the Water Tribe',
                16: 'The Deserter',
                17: 'The Northern Air Temple',
                18: 'The Waterbending Master',
                '19/20': 'The Siege of the North',  # TODO: Should multi-part episodes really be separated?
                21: 'The Avatar State',
                22: 'The Cave of Two Lovers',
                23: 'Return to Omashu',
                24: 'The Swamp',
                25: 'Avatar Day',
                26: 'The Blind Bandit',
                27: 'Zuko Alone',
                28: 'The Chase',
                29: 'Bitter Work',
                30: 'The Library',
                31: 'The Desert',
                32: "The Serpent's Pass",
                33: 'The Drill',
                34: 'City of Walls and Secrets',
                35: 'The Tales of Ba Sing Se',
                36: "Appa's Lost Days",
                37: 'Lake Laogai',
                38: 'The Earth King',
                39: 'The Guru',
                40: 'The Crossroads of Destiny',
                41: 'The Awakening',
                42: 'The Headband',
                43: 'The Painted Lady',
                44: "Sokka's Master",
                45: 'The Beach',
                46: 'The Avatar and the Fire Lord',
                47: 'The Runaway',
                48: 'The Puppetmaster',
                49: 'Nightmares and Daydreams',
                '50/51': 'The Day of Black Sun',
                52: 'The Western Air Temple',
                53: 'The Firebending Masters',
                '54/55': 'The Boiling Rock',
                56: 'The Southern Raiders',
                57: 'The Ember Island Players',
                '58-61': "Sozin's Comet"})

show.plot_threads = [
    (1, 2, Plot.SERIAL, "Zuko attacking the water tribe"),
    (2, 3, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 4, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 5, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 6, Plot.CAUSAL, "Journey to the North Pole"),
    (2, '7/8', Plot.CAUSAL, "Journey to the North Pole"),
    (3, '7/8', Plot.REFERENTIAL, "Admiral Zhao"),  # Really, probably shouldn't be treated differently from Zuko at this point
    ('7/8', 9, Plot.CAUSAL, "Aang attempting to master all four elements"),
    (2, 10, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 11, Plot.CAUSAL, "Journey to the North Pole"),
    (1, 12, Plot.CAUSAL, "Aang and Zuko's pasts"),
    (2, 12, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 13, Plot.CAUSAL, "Journey to the North Pole"),
    (12, 13, Plot.CAUSAL, "Sokka sick due to the storm"),
    (2, 14, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 15, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 16, Plot.CAUSAL, "Journey to the North Pole"),
    ('7/8', 16, Plot.CAUSAL, "Aang attempting to master all four elements"),
    (2, 17, Plot.CAUSAL, "Journey to the North Pole"),
    (2, 18, Plot.CAUSAL, "Arrival at the North Pole"),
    ('7/8', 18, Plot.CAUSAL, "Aang attempting to master all four elements"),
    (9, 18, Plot.REFERENTIAL, "The pirates"),
    (13, 18, Plot.CAUSAL, "Zuko having freed Aang from Zhao"),
    (18, '19/20', Plot.SERIAL, "Fire nation attack on the Northern Water Tribe, Zuko/Iroh on Zhao's ship"),
    (5, 21, Plot.CAUSAL, "King Bumi as Aang's potential Earthbending teacher"),
    ('7/8', 21, Plot.CAUSAL, "Aang attempting to master all four elements"),
    ('19/20', 21, Plot.CAUSAL, "Aang's bending display during the siege, Zuko/Iroh branded as traitors"),
    (21, 22, Plot.CAUSAL, "Travelling to Omashu"),
    ('19/20', 23, Plot.CAUSAL, "Azula's persual of the Avatar"),
    (22, 23, Plot.CAUSAL, "Omashu under the Fire Nation's control"),
    (13, 24, Plot.REFERENTIAL, "Zuko's Blue Spirit mask"),
    (21, 24, Plot.CAUSAL, "Zuko/Iroh as outcasts"),
    (24, 25, Plot.CAUSAL, "Zuko stealing food"),
    (23, 26, Plot.CAUSAL, "Bumi's advice on selecting an Earthbending teacher"),
    (24, 26, Plot.CAUSAL, "Toph's appearance in Aang's vision"),
    (25, 27, Plot.CAUSAL, "Zuko parting ways from Iroh"),
    (26, 28, Plot.REFERENTIAL, "Toph having joined the gang"),
    ('19/20', 28, Plot.CAUSAL, "Azula's persual of the Avatar"),
    (25, 28, Plot.CAUSAL, "Zuko parting ways from Iroh"),
    (26, 29, Plot.CAUSAL, "Aang Earthbending training with Toph"),
    (28, 29, Plot.CAUSAL, "Zuko training to defeat Azula"),
    ('7/8', 30, Plot.CAUSAL, "Seeking a way to defeat the Fire Lord"),
    (30, 31, Plot.SERIAL, "Attempting to rescue Appa"),
    (4, 32, Plot.REFERENTIAL, "The Kyoshi Warriors"),
    (10, 32, Plot.REFERENTIAL, "Jet"),
    (31, 32, Plot.CAUSAL, "Travelling to Ba Sing Se in search of Appa"),
    (31, 32, Plot.CAUSAL, "Zuko/Iroh and Jet"),
    (32, 33, Plot.SERIAL, "Stopping the fire nation drill"),
    (30, 34, Plot.CAUSAL, "Attempting to inform the Earth King of the eclipse"),
    (33, 34, Plot.CAUSAL, "Searching for Appa"),
    (33, 34, Plot.CAUSAL, "Jet confronting Zuko"),
    (33, 35, Plot.CAUSAL, "The cast in Ba Sing Se"),
    (32, 36, Plot.REFERENTIAL, "The Kyoshi warriors"),
    (31, 36, Plot.SERIAL, "Appa's hardships"),
    (25, 37, Plot.CAUSAL, "Zuko's internal conflict"),
    (34, 37, Plot.SERIAL, "The Dai Li's obstruction, Jet's brainwashing"),
    (36, 37, Plot.SERIAL, "Appa's rescue"),
    (33, 38, Plot.REFERENTIAL, "The drill"),
    (37, 38, Plot.SERIAL, "Warning the Earth King about the war"),
    (26, 39, Plot.CAUSAL, "Xin Fu and Master Yu bounty hunting Toph"),
    (36, 39, Plot.CAUSAL, "The Guru's message to Aang"),
    (38, 39, Plot.CAUSAL, "The Dai Li attempting to regain power"),
    (21, 40, Plot.CAUSAL, "The spirit water"),
    (37, 40, Plot.CAUSAL, "Zuko's internal conflict"),
    (39, 40, Plot.SERIAL, "Azula/the Dai Li's coup"),
    ('7/8', 41, Plot.REFERENTIAL, "Avatar Roku communicating with Aang"),
    ('19/20', 41, Plot.REFERENTIAL, "Yue the moon spirit"),
    (38, 41, Plot.CAUSAL, "Formation of the eclipse invasion plan"),
    (40, 41, Plot.CAUSAL, "Aang believed dead, Zuko welcomed back to the fire nation"),
    (40, 42, Plot.CAUSAL, "Iroh imprisoned, Zuko's internal conflict and suspicion that Aang is alive"),
    (41, 42, Plot.CAUSAL, "Undercover in the fire nation"),
    (41, 43, Plot.CAUSAL, "Undercover in the fire nation"),
    (40, 44, Plot.CAUSAL, "Iroh imprisoned"),
    (41, 44, Plot.CAUSAL, "Undercover in the fire nation"),
    (41, 45, Plot.CAUSAL, "Zuko and Team Azula relaxing"),
    (42, 45, Plot.CAUSAL, "The assassin hired by Zuko"),
    ('7/8', 46, Plot.REFERENTIAL, "Avatar Roku visiting Aang"),
    (42, 46, Plot.CAUSAL, "Zuko's internal conflict"),
    #(?, 46, Plot.CAUSAL, "Backstory of the fire nation and the previous avatar"),  # TODO: Still not sure how to handle backstories
    (41, 47, Plot.CAUSAL, "Undercover in the fire nation"),
    (42, 47, Plot.CAUSAL, "The assassin hired by Zuko"),
    (41, 48, Plot.CAUSAL, "Undercover in the fire nation"),
    (41, 49, Plot.CAUSAL, "The invasion plan"),
    (46, 49, Plot.CAUSAL, "Zuko's internal conflict"),  # Character
    (39, '50/51', Plot.REFERENTIAL, "Zuko's lightning redirection"),  # Causal?
    (36, '50/51', Plot.CAUSAL, "Suki's capture"),
    (41, '50/51', Plot.SERIAL, "The invasion plan"),
    (44, '50/51', Plot.CAUSAL, "Iroh's escape"),
    (49, '50/51', Plot.CAUSAL, "Zuko's internal conflict"),  # It gets a bit subjective whether these are serial but eh
    (42, '50/51', Plot.CAUSAL, "The assassin hired by Zuko"),
    ('50/51', 52, Plot.CAUSAL, "Zuko seeking to join Team Avatar"),
    ('7/8', 53, Plot.CAUSAL, "Aang attempting to master all four elements"),
    (52, 53, Plot.CAUSAL, "Zuko on Team Avatar"),
    #(?, '54/55', Plot.CAUSAL, "Zuko/Mai's relationship"),
    ('50/51', '54/55', Plot.CAUSAL, "Rescuing Suki"),
    (52, '54/55', Plot.CAUSAL, "Zuko on Team Avatar"),
    (52, 56, Plot.CAUSAL, "Katara's distrust of Zuko"),
    ('7/8', '58-61', Plot.CAUSAL, "Arrival of Sozin's Comet"),
    (31, '58-61', Plot.CAUSAL, "Iroh's connection to a secret society"),
    ('50/51', '58-61', Plot.CAUSAL, "Aang/Katara's relationship"),
    ('54/55', '58-61', Plot.CAUSAL, "Azula starting to lose her sanity after Mai/Ty Lee's betrayal")]

show.foreshadowing = [
    (9, '58-61', Foreshadowing.MAJOR, "Importance of the white lotus Pai Sho tile to Iroh; Order of the White Lotus"),
    (30, '58-61', Foreshadowing.MAJOR, "Book about Lion-Turtles in the library"),
    (17, 32, Foreshadowing.MAJOR, "Schematics for the drill seen"),
    (33, 39, Foreshadowing.MAJOR, '''"What I'd give to be a metalbender"'''),
    (44, '58-61', Foreshadowing.MAJOR, "White lotus Pai Sho tile gifted to Sokka; Order of the White Lotus")]
