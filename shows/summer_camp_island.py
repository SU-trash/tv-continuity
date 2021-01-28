#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''Continuity data on the show Summer Camp Island.'''

from show_continuity import *

show = Show(
    title='Summer Camp Island',
    seasons={
        1: {'color': '#E698D0',
            'episodes': {
                'S1E1': 'The First Day',
                'S1E2': 'Monster Babies',
                'S1E3': 'Chocolate MoneyBadgers',
                'S1E4': 'Saxophone ComeHome',
                'S1E5': 'Pajama Pajimjams',
                'S1E6': "Oscar & Hedgehog's Melody",
                'S1E7': 'Feeling Spacey',
                'S1E8': 'Ghost the Boy',
                'S1E9': 'Computer Vampire',
                'S1E10': 'The Basketball Liaries',
                'S1E11': 'Popular Banana Split',
                'S1E12': 'Time Traveling Quick Pants',
                'S1E13': "It's My Party",
                'S1E14': 'Moon Problems',
                'S1E15': 'Monster Visit',
                'S1E16': 'Ice Cream Headache',
                'S1E17': "Pepper's Blanket IsMissing",
                'S1E18': 'Hedgehog Werewolf',
                'S1E19': 'Mr. Softball',
                'S1E20': 'Fuzzy Pink TimeBabies',
                'S1E21': 'Cosmic Bupkiss',
                'S1E22': 'Radio Silence',
                'S1E23': "Director's Cut",
                'S1E24': 'The Haunted Campfire',
                'S1E25': 'I Heart Heartforde',
                'S1E26': 'Space Invasion',
                'S1E27': 'Mom Soon',
                'S1E28': 'Sneeze Guard',
                'S1E29': "Susie's Fantastical Scavenger Hunt",
                'S1E30': 'Mop Forever',
                'S1E31': 'Pajamas Party',
                'S1E32': 'The Soundhouse',
                'S1E33': 'Puff Paint',
                'S1E34': 'Susie Appreciation Day',
                'S1E35': 'Campers Above the Bed',
                'S1E36': 'Midnight Quittance',
                'S1E37': 'The Great Elf Invention Convention',
                'S1E38': 'Twelve Angry Hedgehogs',
                'S1E39': 'Spell Crushers',
                'S1E40': 'The Library'}},
        2: {'color': '#AADAD3',
            'episodes': {
                'S2E1': 'Meeting of the Minds',
                'S2E2': "Ava's Yard Sale",
                'S2E3': 'Molar Moles',
                'S2E4': 'Tortilla Towel',
                'S2E5': 'Acorn Graduation',
                'S2E6': 'Dungeon Doug',
                'S2E7': 'Tub on the Run',
                'S2E8': 'Spotted Bear Stretch',
                'S2E9': 'French Toasting',
                'S2E10': "We'll Just Move the Stars",
                'S2E11': 'Catacombs',
                'S2E12': "Wild Hearts Can't Be Caboodled",
                'S2E13': 'The Later Pile',
                'S2E14': 'Honeydew Hatch',
                'S2E15': 'Light as a Feather',
                'S2E16': 'When Harry Met Barry',
                'S2E17': 'Oddjobs',
                'S2E18': 'Tumble Dry Low',
                'S2E19': 'Just You and Me',
                'S2E20': 'Glow Worm'}},
        3: {'color': '#a2a9b1',
            'episodes': {
                'S3E1': "Susie and Ramona Chapter 1: Susie's Ark",
                'S3E2': 'Susie and Ramona Chapter 2: Ghost Baby Jabberwock',
                'S3E3': 'Susie and Ramona Chapter 3: Meet Me in Massachusetts',
                'S3E4': 'Susie and Ramona Chapter 4: Witches in the City',
                'S3E5': 'Puddle and the King Chapter 1: Honey Moondog',
                'S3E6': 'Puddle and the King Chapter 2: Royally Bored',
                'S3E7': "Puddle and the King Chapter 3: All the King's Slides",
                'S3E8': 'Yeti Confetti Chapter One: Don’t Tell Lucy',
                'S3E9': 'Yeti Confetti Chapter Two: The Yum Whisperer',
                'S3E10': 'Yeti Confetti Chapter Three: The Sherbet Scoop',
                'S3E11': "Yeti Confetti Chapter Four: Lucy's Instrument",
                'S3E12': "Yeti Confetti Chapter Five: Where's the Confetti"}}})

show.plot_threads = [
    ('S1E3', 'S1E14', Plot.REFERENTIAL, 'Moon friendship bracelet'),
    ('S1E20', 'S1E21', Plot.CAUSAL, "Ramona & Susie's past"),
    ('S1E22', 'S1E27', Plot.REFERENTIAL, "Oscar/HH's Radio show"),
    ('S1E30', 'S1E31', Plot.REFERENTIAL, 'HH casts a spell'),
    ('S1E18', 'S1E32', Plot.REFERENTIAL, 'HH being a werewolf'),
    ('S1E21', 'S1E34', Plot.CAUSAL, "Ramona & Susie's past"),
    ('S1E20', 'S1E36', Plot.REFERENTIAL, 'Ramona'),
    ('S1E32', 'S1E37', Plot.REFERENTIAL, 'Barb'),
    ('S1E30', 'S1E39', Plot.CAUSAL, 'HH learning to be a witch'),
    ('S1E35', 'S1E39', Plot.CAUSAL, "HH's crush on Max"),
    ('S1E39', 'S1E40', Plot.REFERENTIAL, 'HH learning magic'),
    ('S1E40', 'S2E1', Plot.SERIAL, "Susie having confiscated HH's wand"),
    ('S1E30', 'S2E5', Plot.CAUSAL, "HH learning to be a witch"),
    ('S1E39', 'S2E7', Plot.CAUSAL, "HH having confessed to Max"),
    ('S1E4', 'S2E11', Plot.REFERENTIAL, 'Saxophone'),
    ('S1E30', 'S2E12', Plot.CAUSAL, "HH learning to be a witch"),
    ('S1E34', 'S2E14', Plot.CAUSAL, "Ramona & Susie's falling out"),
    ('S1E30', 'S2E15', Plot.CAUSAL, "HH learning to be a witch"),
    ('S1E22', 'S2E18', Plot.REFERENTIAL, "HH's radio show"),
    ('S1E18', 'S2E19', Plot.REFERENTIAL, "Betsy being a werewolf"),
    ('S1E18', 'S2E20', Plot.REFERENTIAL, "HH being a werewolf"),
    ('S1E30', 'S2E20', Plot.REFERENTIAL, "HH learning to be a witch"),
    ('S3E1', 'S3E2', Plot.SERIAL, "Susie and Ramona founding the island"),
    ('S3E2', 'S3E3', Plot.SERIAL, "Susie and Ramona founding the island"),
    ('S3E3', 'S3E4', Plot.CAUSAL, "Susie and Ramona founding the island / Ramona trapped in frozen time"),
    ('S3E4', 'S1E1', Plot.SERIAL, "The campers having been invited to the island"),
    ('S3E5', 'S3E6', Plot.CAUSAL, "Oscar/HH kingdom-sitting for King/Puddle"),
    ('S3E5', 'S3E7', Plot.CAUSAL, "Oscar/HH kingdom-sitting for King/Puddle"),
    ('S3E8', 'S3E10', Plot.REFERENTIAL, "Yeti Confetti"),
    ('S3E8', 'S3E11', Plot.CAUSAL, "Lucy's yeti heritage"),
    ('S3E8', 'S3E12', Plot.CAUSAL, "Lucy's yeti heritage")]

