#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Amphibia.'''

show = Show(
    title='Amphibia',
    # Season colors from https://en.wikipedia.org/wiki/Amphibia_(TV_series)#Episodes
    seasons={1: dict(num_eps=39, color='#3CB371')},
    episodes={
        'S1E1a': 'Anne or Beast?',
        'S1E1b': 'Best Fronds',
        'S1E2a': 'Cane Crazy',
        'S1E2b': 'Flood, Sweat and Tears',
        'S1E3a': 'Hop Luck',
        'S1E3b': 'Stakeout',
        'S1E4a': 'The Domino Effect',
        'S1E4b': 'Taking Charge',
        'S1E5a': 'Anne Theft Auto',
        'S1E5b': 'Breakout Star',
        'S1E6a': 'Sprig Vs. Hop Pop',
        'S1E6b': 'Girl Time',
        'S1E7a': 'Dating Season',
        'S1E7b': 'Anne Vs. Wild',
        'S1E8a': 'Contagi-Anne',
        'S1E8b': 'Family Shrub',
        'S1E9a': 'Lily Pad Thai',
        'S1E9b': 'Plantar’s Last Stand',
        'S1E10a': 'Toad Tax',
        'S1E10b': 'Prison Break',
        'S1E11a': 'Grubhog Day',
        'S1E11b': 'Hop Pop and Lock',
        'S1E12a': 'Civil Wart',
        'S1E12b': 'Hop-Popular',
        'S1E13a': 'Croak and Punishment',
        'S1E13b': 'Trip to the Archives',
        'S1E14a': 'Snow Day',
        'S1E14b': 'Cracking Mrs. Croaker',
        'S1E15a': 'A Night at The Inn',
        'S1E15b': 'Wally and Anne',
        'S1E16a': 'Family Fishing Trip',
        'S1E16b': 'Bizarre Bazaar',
        'S1E17a': 'Cursed!',
        'S1E17b': 'Fiddle Me This',
        'S1E18a': 'The Big Bugball Game',
        'S1E18b': 'Combat Camp',
        'S1E19a': 'Children of the Spore',
        'S1E19b': 'Anne of the Year',
        'S1E20': 'Reunion'})

show.plot_threads = [
    ('S1E1a', 'S1E1b', Plot.CAUSAL, "Anne trapped in Amphibia / Anne's homesickness"),
    ('S1E1a', 'S1E7b', Plot.CAUSAL, 'Music box arc'),
    ('S1E1b', 'S1E10b', Plot.CAUSAL, 'Sasha arc'),
    ('S1E9b', 'S1E12b', Plot.CAUSAL, "The Plantar's losing their vegetable stand"),
    ('S1E7b', 'S1E16b', Plot.CAUSAL, 'Music box arc'),
    ('S1E3a', 'S1E17a', Plot.CAUSAL, "Sprig's engagement to Maddie"),
    ('S1E7a', 'S1E19b', Plot.CAUSAL, "Sprig's crush on Ivy"),
    ('S1E10b', 'S1E19b', Plot.CAUSAL, 'Sasha arc'),
    ('S1E19b', 'S1E20', Plot.SERIAL, "Grime/Sasha's invasion")]
