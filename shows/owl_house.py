#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show The Owl House.'''

show = Show(
    title='The Owl House',
    brief_title='Owl House',
    seasons={
        1: {'color': '#FADA5E',
            'episodes': {
                'S1E1': 'A Lying Witch and a Warden',
                'S1E2': 'Witches Before Wizards',
                'S1E3': 'I Was a Teenage Abomination',
                'S1E4': 'The Intruder',
                'S1E5': 'Covention',
                'S1E6': "Hooty's Moving Hassle",
                'S1E7': 'Lost in Language',
                'S1E8': 'Once Upon a Swap',
                'S1E9': 'Something Ventured, Someone Framed',
                'S1E10': 'Escape of the Palisman',
                'S1E11': 'Adventures in the Elements'}}})

show.plot_threads = [
    # Ep 1 is technically causal to every episode of the show but doesn't matter for our seriality metric (by design)
    ('S1E1', 'S1E4', Plot.CAUSAL, "Luz entering the Boiling Isles and becoming Eda's apprentice"),
    ('S1E3', 'S1E5', Plot.REFERENTIAL, "Luz and Amity's rivalry"),
    ('S1E4', 'S1E5', Plot.REFERENTIAL, "Luz' light spell"),
    ('S1E4', 'S1E5', Plot.REFERENTIAL, "Eda's curse"),
    ('S1E4', 'S1E6', Plot.CAUSAL, "Eda's curse"),
    ('S1E5', 'S1E7', Plot.CAUSAL, 'Luz/Amity relationship development'),
    ('S1E5', 'S1E8', Plot.REFERENTIAL, "Eda and Lilith / Emperor's Coven"),
    ('S1E3', 'S1E9', Plot.CAUSAL, 'Luz wanting to enrol in Hexside / heightened Hexside security'),
    ('S1E4', 'S1E10', Plot.CAUSAL, "Eda's Curse"),
    ('S1E7', 'S1E10', Plot.REFERENTIAL, 'The Bat Queen and her children'),
    ('S1E7', 'S1E11', Plot.REFERENTIAL, "Luz/Amity's friendship, Emira & Edric making up for the library incident"),
    ('S1E9', 'S1E11', Plot.CAUSAL, 'Luz preparing to go to Hexside')]
