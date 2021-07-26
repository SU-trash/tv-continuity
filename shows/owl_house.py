#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show The Owl House.'''

show = Show(
    title='The Owl House',
    brief_title='Owl House',
    # Season colors / episode titles from https://en.wikipedia.org/wiki/The_Owl_House_(TV_series)#Episodes
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
                'S1E11': 'Sense and Insensitivity',
                'S1E12': 'Adventures in the Elements',
                'S1E13': 'The First Day',
                'S1E14': 'Really Small Problems',
                'S1E15': 'Understanding Willow',
                'S1E16': 'Enchanting Grom Fright',
                'S1E17': 'Wing It Like Witches',
                'S1E18': 'Agony of a Witch',
                'S1E19': 'Young Blood, Old Souls'}},
        2: {'color': '#942C2C',
            'episodes': {
                'S2E1': "Separate Tides",
                'S2E2': "Escaping Expulsion",
                'S2E3': "Echoes of the Past",
                'S2E4': "Keeping Up A-fear-ances",
                'S2E5': "Through the Looking Glass Ruins",
                'S2E6': "Hunting Palismen",
                'S2E7': "Eda's Requiem",
                'S2E8': "Knock, Knock, Knockin' on Hooty's Door"}}})

show.plot_threads = [
    # S1E1 is technically causal to every episode of the show but doesn't affect our seriality metric (by design)
    ('S1E1', 'S1E4', Plot.CAUSAL, "Luz entering the Boiling Isles and becoming Eda's apprentice"),
    ('S1E3', 'S1E5', Plot.REFERENTIAL, "Luz and Amity's rivalry"),
    ('S1E4', 'S1E5', Plot.REFERENTIAL, "Luz' light spell"),
    ('S1E4', 'S1E5', Plot.REFERENTIAL, "Eda's curse"),
    ('S1E4', 'S1E6', Plot.CAUSAL, "Eda's curse"),
    ('S1E5', 'S1E7', Plot.CAUSAL, "Luz/Amity's rivalry"),
    ('S1E5', 'S1E8', Plot.REFERENTIAL, "Eda and Lilith / Emperor's Coven"),
    ('S1E3', 'S1E9', Plot.CAUSAL, 'Luz wanting to enrol in Hexside / heightened Hexside security'),
    ('S1E4', 'S1E10', Plot.CAUSAL, "Eda's curse"),
    ('S1E7', 'S1E10', Plot.REFERENTIAL, 'The Bat Queen and her children'),
    ('S1E5', 'S1E11', Plot.REFERENTIAL, "Eda and Lilith / Emperor's Coven"),
    ('S1E7', 'S1E12', Plot.REFERENTIAL, "Luz/Amity's friendship, Luz having lent Amity a book"),
    ('S1E9', 'S1E12', Plot.CAUSAL, 'Luz preparing to attend Hexside'),
    ('S1E9', 'S1E13', Plot.CAUSAL, 'Luz beginning to attend Hexside'),
    ('S1E13', 'S1E14', Plot.REFERENTIAL, 'Luz attending Hexside'),
    ('S1E13', 'S1E15', Plot.CAUSAL, 'Luz attending Hexside'),
    ('S1E6', 'S1E15', Plot.REFERENTIAL, "Willow and Amity's past"),
    ('S1E7', 'S1E16', Plot.CAUSAL, "Luz/Amity's friendship"),
    ('S1E13', 'S1E16', Plot.CAUSAL, 'Luz attending Hexside'),
    ('S1E13', 'S1E17', Plot.CAUSAL, 'Luz attending Hexside'),
    ('S1E15', 'S1E17', Plot.REFERENTIAL, "Willow's increased confidence"),
    ('S1E16', 'S1E17', Plot.REFERENTIAL, "Amity's worsening gay panic"),
    ('S1E5', 'S1E18', Plot.CAUSAL, "Eda and Lilith / Emperor's Coven"),
    ('S1E10', 'S1E18', Plot.CAUSAL, "Eda's curse worsening"),
    ('S1E13', 'S1E18', Plot.CAUSAL, "Luz attending Hexside"),
    ('S1E17', 'S1E18', Plot.REFERENTIAL, "Amity's broken leg"),
    ('S1E17', 'S1E19', Plot.REFERENTIAL, "Amity's broken leg"),
    ('S1E18', 'S1E19', Plot.SERIAL, "Eda captured by the Emperor's Coven / Eda/Lilith and the curse"),
    ('S1E19', 'S2E1', Plot.CAUSAL, "Eda/Lilith reconciled and their weakened magic"),
    ('S1E19', 'S2E2', Plot.CAUSAL, "Eda/Lilith reconciled and their weakened magic"),
    ('S1E16', 'S2E2', Plot.CAUSAL, "Amity's deepening friendship with the gang / grom photo"),
    ('S1E18', 'S2E4', Plot.CAUSAL, "Origin of the curse"),
    ('S1E19', 'S2E4', Plot.CAUSAL, "Eda/Lilith reconciled and their shared curse"),
    ('S2E3', 'S2E4', Plot.REFERENTIAL, "King learning of his origin"),
    ('S1E9', 'S2E5', Plot.REFERENTIAL, "Mattholomule/Gus' rivalry"),
    ('S2E4', 'S2E5', Plot.CAUSAL, "Luz learning of a past human in the Boiling Isles"),
    ('S1E16', 'S2E5', Plot.CAUSAL, "Amity/Luz' worsening gay panic"),
    ('S1E10', 'S2E6', Plot.REFERENTIAL, "The Bat Queen and the orphaned palismans"),
    ('S2E3', 'S2E7', Plot.CAUSAL, "King learning of his origin"),
    ('S2E4', 'S2E7', Plot.REFERENTIAL, "The echo mouse"),
    ('S2E3', 'S2E8', Plot.CAUSAL, "King learning of his origin"),
    ('S1E19', 'S2E8', Plot.CAUSAL, "Eda's weakened magic / the curse"),
    ('S2E7', 'S2E8', Plot.REFERENTIAL, "Eda/Raine's relationship"),
    ('S2E5', 'S2E8', Plot.CAUSAL, "The Echo Mouse / Philip Wittebane's journal"),
    ('S2E5', 'S2E8', Plot.CAUSAL, "Amity/Luz' worsening gay panic 2")]

show.foreshadowing = [
    ('S1E7', 'S1E16', Foreshadowing.MAJOR, "Amity's hideout being in the romance section", "Amity's crush on Luz"),
    #('S2E6', ?, Foreshadowing.MAJOR, "Most of Hunter's ancestors having been unable to use magic",
    #                                 "Hunter descended from Philip Wittebane"),
]
