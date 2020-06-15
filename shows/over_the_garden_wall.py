#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Over the Garden Wall.'''

show = Show(
    title='Over the Garden Wall',
    brief_title='Over the Garden Wall',
    seasons={
        1: {'color': '#804060',
            'episodes': {
                'S1E1': 'The Old Grist Mill',
                'S1E2': "Hard Times at the Huskin' Bee",
                'S1E3': 'Schooltown Follies',
                'S1E4': 'Songs of the Dark Lantern',
                'S1E5': 'Mad Love',
                'S1E6': 'Lullaby in Frogland',
                'S1E7': 'The Ringing of the Bell',
                'S1E8': 'Babes in the Wood',
                'S1E9': 'Into the Unknown',
                'S1E10': 'The Unknown'}}})

show.plot_threads = [
    ('S1E1', 'S1E2', Plot.REFERENTIAL, 'The bluebird'),
    ('S1E2', 'S1E3', Plot.CAUSAL, 'Searching for Adelaide'),
    ('S1E1', 'S1E4', Plot.REFERENTIAL, 'The Beast and the Woodsman'),
    ('S1E2', 'S1E4', Plot.CAUSAL, 'Searching for Adelaide'),
    ('S1E2', 'S1E5', Plot.CAUSAL, 'Searching for Adelaide'),
    ('S1E5', 'S1E2', Plot.CAUSAL, "Beatrice's backstory"),
    ('S1E5', 'S1E6', Plot.CAUSAL, 'Catching the ferry'),
    ('S1E6', 'S1E8', Plot.CAUSAL, "Beatrice's return"),
    ('S1E8', 'S1E9', Plot.CAUSAL, 'Rescuing Greg'),
    ('S1E4', 'S1E10', Plot.CAUSAL, "The Beast's lies"),
    ('S1E9', 'S1E10', Plot.CAUSAL, 'Rescuing Greg')]
