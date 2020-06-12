#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Amphibia.'''

show = Show(
    title='Amphibia',
    # Season colors from https://en.wikipedia.org/wiki/Amphibia_(TV_series)#Episodes
    seasons={1: dict(num_eps=39, color='#3CB371')},
    episodes={
        '1a': 'Anne or Beast?',
        '1b': 'Best Fronds',
        '2a': 'Cane Crazy',
        '2b': 'Flood, Sweat and Tears',
        '3a': 'Hop Luck',
        '3b': 'Stakeout',
        '4a': 'The Domino Effect',
        '4b': 'Taking Charge',
        '5a': 'Anne Theft Auto',
        '5b': 'Breakout Star',
        '6a': 'Sprig Vs. Hop Pop',
        '6b': 'Girl Time',
        '7a': 'Dating Season',
        '7b': 'Anne Vs. Wild',
        '8a': 'Contagi-Anne',
        '8b': 'Family Shrub',
        '9a': 'Lily Pad Thai',
        '9b': 'Plantar’s Last Stand',
        '10a': 'Toad Tax',
        '10b': 'Prison Break',
        '11a': 'Grubhog Day',
        '11b': 'Hop Pop and Lock',
        '12a': 'Civil Wart',
        '12b': 'Hop-Popular',
        '13a': 'Croak and Punishment',
        '13b': 'Trip to the Archives',
        '14a': 'Snow Day',
        '14b': 'Cracking Mrs. Croaker',
        '15a': 'A Night at The Inn',
        '15b': 'Wally and Anne',
        '16a': 'Family Fishing Trip',
        '16b': 'Bizarre Bazaar',
        '17a': 'Cursed!',
        '17b': 'Fiddle Me This',
        '18a': 'The Big Bugball Game',
        '18b': 'Combat Camp',
        '19a': 'Children of the Spore',
        '19b': 'Anne of the Year',
        20: 'Reunion'})

show.plot_threads = [
    ('1a', '1b', Plot.CAUSAL, "Anne trapped in Amphibia / Anne's homesickness"),
    ('1a', '7b', Plot.CAUSAL, "Music box arc"),
    ('1b', '10b', Plot.CAUSAL, "Sasha arc"),
    ('9b', '12b', Plot.CAUSAL, "The Plantar's losing their vegetable stand"),
    ('7b', '16b', Plot.CAUSAL, "Music box arc"),
    ('3a', '17a', Plot.CAUSAL, "Sprig's engagement to Maddie"),
    ('7a', '19b', Plot.CAUSAL, "Sprig's crush on Ivy"),
    ('10b', '19b', Plot.CAUSAL, "Sasha arc"),
    ('19b', 20, Plot.SERIAL, "Grime/Sasha's invasion")]
