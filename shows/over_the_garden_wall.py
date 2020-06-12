#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Over the Garden Wall.'''

show = Show(
    title='Over the Garden Wall',
    brief_title='Over the Garden Wall',
    seasons={1: dict(num_eps=10, color='#804060')},
    episodes={
        1: 'The Old Grist Mill',
        2: "Hard Times at the Huskin' Bee",
        3: 'Schooltown Follies',
        4: 'Songs of the Dark Lantern',
        5: 'Mad Love',
        6: 'Lullaby in Frogland',
        7: 'The Ringing of the Bell',
        8: 'Babes in the Wood',
        9: 'Into the Unknown',
        10: 'The Unknown'})

show.plot_threads = [
    (1, 2, Plot.REFERENTIAL, "The bluebird"),
    (2, 3, Plot.CAUSAL, "Searching for Adelaide"),
    (1, 4, Plot.REFERENTIAL, "The Beast and the Woodsman"),
    (2, 4, Plot.CAUSAL, "Searching for Adelaide"),
    (2, 5, Plot.CAUSAL, "Searching for Adelaide / Beatrice's backstory"),
    (5, 6, Plot.CAUSAL, "Catching the ferry"),
    (6, 8, Plot.CAUSAL, "Beatrice's return"),
    (8, 9, Plot.CAUSAL, "Rescuing Greg"),
    (4, 10, Plot.CAUSAL, "The Beast's lies"),
    (9, 10, Plot.CAUSAL, "Rescuing Greg")]

show.foreshadowing = []
