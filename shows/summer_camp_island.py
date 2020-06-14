#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''Continuity data on the show Summer Camp Island.'''

from show_continuity import *

show = Show(
    title='Summer Camp Island',
    seasons={1: dict(num_eps=40, color='#E698D0')},
    episodes={
        1: 'The First Day',
        2: 'Monster Babies',
        3: 'Chocolate MoneyBadgers',
        4: 'Saxophone ComeHome',
        5: 'Pajama Pajimjams',
        6: "Oscar & Hedgehog's Melody",
        7: 'Feeling Spacey',
        8: 'Ghost the Boy',
        9: 'Computer Vampire',
        10: 'The Basketball Liaries',
        11: 'Popular Banana Split',
        12: 'Time Traveling Quick Pants',
        13: "It's My Party",
        14: 'Moon Problems',
        15: 'Monster Visit',
        16: 'Ice Cream Headache',
        17: "Pepper's Blanket IsMissing",
        18: 'Hedgehog Werewolf',
        19: 'Mr. Softball',
        20: 'Fuzzy Pink TimeBabies',
        21: 'Cosmic Bupkiss',
        22: 'Radio Silence',
        23: "Director's Cut",
        24: 'The Haunted Campfire',
        25: 'I Heart Heartforde',
        26: 'Space Invasion',
        27: 'Mom Soon',
        28: 'Sneeze Guard',
        29: "Susie's Fantastical Scavenger Hunt",
        30: 'Mop Forever',
        31: 'Pajamas Party',
        32: 'The Soundhouse',
        33: 'Puff Paint',
        34: 'Susie Appreciation Day',
        35: 'Campers Above the Bed',
        36: 'Midnight Quittance',
        37: 'The Great Elf Invention Convention',
        38: 'Twelve Angry Hedgehogs',
        39: 'Spell Crushers',
        40: 'The Library'})

show.plot_threads = [
    (3, 14, Plot.REFERENTIAL, r'''Moon friendship bracelet'''),
    (20, 21, Plot.CAUSAL, r'''Ramona & Susie's past'''),
    (22, 27, Plot.REFERENTIAL, r'''Oscar/HH's Radio show'''),
    (30, 31, Plot.REFERENTIAL, r'''HH casts a spell'''),
    (18, 32, Plot.REFERENTIAL, r'''HH being a werewolf'''),
    (21, 34, Plot.CAUSAL, r'''Ramona & Susie's past'''),
    (20, 36, Plot.REFERENTIAL, r'''Ramona'''),
    (32, 37, Plot.REFERENTIAL, r'''Barb'''),
    (30, 39, Plot.CAUSAL, r'''HH learning to be a witch'''),
    (35, 39, Plot.CAUSAL, r'''HH's crush on Max'''),
    (39, 40, Plot.REFERENTIAL, r'''HH learning magic''')]
