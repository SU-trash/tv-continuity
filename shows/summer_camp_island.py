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
                'S1E40': 'The Library'}}})

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
    ('S1E39', 'S1E40', Plot.REFERENTIAL, 'HH learning magic')]
