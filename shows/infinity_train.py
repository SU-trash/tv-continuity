#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Infinity Train.'''

show = Show(
    title='Infinity Train',
    # Season colors from https://en.wikipedia.org/wiki/List_of_Infinity_Train_episodes
    seasons={1: dict(num_eps=10, color='#534DA1'),
             2: dict(num_eps=10, color='#9A9A75')},
    episodes={
        'S1E1': 'The Grid Car',
        'S1E2': 'The Beach Car',
        'S1E3': 'The Corgi Car',
        'S1E4': 'The Crystal Car',
        'S1E5': "The Cat's Car",
        'S1E6': 'The Unfinished Car',
        'S1E7': 'The Chrome Car',
        'S1E8': 'The Ball Pit Car',
        'S1E9': 'The Past Car',
        'S1E10': 'The Engine',
        'S2E1': 'The Black Market Car',
        'S2E2': 'The Family Tree Car',
        'S2E3': 'The Map Car',
        'S2E4': 'The Toad Car',
        'S2E5': 'The Parasite Car',
        'S2E6': 'The Lucky Cat Car',
        'S2E7': 'The Mall Car',
        'S2E8': 'The Wasteland',
        'S2E9': 'The Tape Car',
        'S2E10': 'The Number Car'})

show.plot_threads = [
    ('S1E1', 'S1E2', Plot.CAUSAL, 'Tulip trapped on the train'),
    ('S1E3', 'S1E5', Plot.CAUSAL, 'The Steward/Conductor trying to stop Tulip'),
    ('S1E3', 'S1E8', Plot.CAUSAL, 'The Steward/Conductor trying to stop Tulip'),
    ('S1E8', 'S1E9', Plot.SERIAL, 'Loss of Atticus'),
    ('S1E8', 'S1E9', Plot.CAUSAL, "The Conductor's betrayal of The Cat"),
    ('S1E2', 'S1E10', Plot.REFERENTIAL, 'The Donut Holer'),
    ('S1E9', 'S1E10', Plot.SERIAL, 'Plan to save Atticus'),
    ('S1E9', 'S1E10', Plot.CAUSAL, 'Amelia having taken over the train'),
    ('S1E7', 'S2E1', Plot.CAUSAL, 'Mirror Tulip'),
    ('S2E1', 'S2E2', Plot.SERIAL, 'MT/Jesse fighting over Alan Dracula'),
    ('S2E2', 'S2E3', Plot.CAUSAL, 'MT helping Jesse escape the train'),
    ('S2E3', 'S2E4', Plot.SERIAL, 'The reflection police attacking the group'),
    ('S2E2', 'S2E5', Plot.CAUSAL, 'MT helping Jesse escape the train'),
    ('S2E2', 'S2E6', Plot.CAUSAL, 'MT helping Jesse escape the train'),
    ('S2E6', 'S2E7', Plot.SERIAL, "Grace's gang"),
    ('S2E7', 'S2E8', Plot.SERIAL, 'Reflection police attacking MT'),
    ('S2E7', 'S2E8', Plot.SERIAL, 'Jesse gone'),
    ('S2E8', 'S2E9', Plot.SERIAL, "MT's plan to get a number"),
    ('S2E9', 'S2E10', Plot.SERIAL, 'MT confronting One-One')]

show.foreshadowing = [
    ('S1E1', 'S1E5', Foreshadowing.MAJOR, 'Conductor briefly flashes by in background when Tulip wakes up; Existence of the Conductor'),
    ('S1E3', 'S1E8', Foreshadowing.MAJOR, r'''"I'll just keep your obituary on file then"; Atticus' death'''),
    ('S1E3', 'S1E10', Foreshadowing.MAJOR, 'The Steward leaving after seeing One-One; One-One is the Conductor'),
    ('S1E6', 'S1E10', Foreshadowing.MAJOR, 'One-One feeling the unfinished car is his fault; One-One is the Conductor'),
    ('S1E9', 'S1E10', Foreshadowing.MAJOR, 'One-One able to easily control the memory tape; One-One is the Conductor'),
    ('S1E10', 'S2E6', Foreshadowing.MAJOR, 'Grace in the passenger list'),
    ('S1E10', 'S2E7', Foreshadowing.MAJOR, 'Simon in the passenger list')]
