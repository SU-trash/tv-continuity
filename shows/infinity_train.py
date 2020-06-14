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
        1: 'The Grid Car',
        2: 'The Beach Car',
        3: 'The Corgi Car',
        4: 'The Crystal Car',
        5: "The Cat's Car",
        6: 'The Unfinished Car',
        7: 'The Chrome Car',
        8: 'The Ball Pit Car',
        9: 'The Past Car',
        10: 'The Engine',
        11: 'The Black Market Car',
        12: 'The Family Tree Car',
        13: 'The Map Car',
        14: 'The Toad Car',
        15: 'The Parasite Car',
        16: 'The Lucky Cat Car',
        17: 'The Mall Car',
        18: 'The Wasteland',
        19: 'The Tape Car',
        20: 'The Number Car'})

show.plot_threads = [
    # Ep 1 is technically causal to every episode of S1, but doesn't matter for our seriality metric (by design)
    (1, 2, Plot.CAUSAL, "Tulip trapped on the train"),
    (3, 5, Plot.CAUSAL, "The Steward/Conductor trying to stop Tulip"),
    (3, 8, Plot.CAUSAL, "The Steward/Conductor trying to stop Tulip"),
    (8, 9, Plot.SERIAL, "Loss of Atticus"),
    (8, 9, Plot.CAUSAL, "The Conductor's betrayal of The Cat"),
    (2, 10, Plot.REFERENTIAL, "The Donut Holer"),
    (9, 10, Plot.SERIAL, "Plan to save Atticus"),
    (9, 10, Plot.CAUSAL, "Amelia having taken over the train"),
    (7, 11, Plot.CAUSAL, "Mirror Tulip"),
    (11, 12, Plot.SERIAL, "MT/Jesse fighting over Alan Dracula"),
    (12, 13, Plot.CAUSAL, "MT helping Jesse escape the train"),
    (13, 14, Plot.SERIAL, "The reflection police attacking the group"),
    (12, 15, Plot.CAUSAL, "MT helping Jesse escape the train"),
    (12, 16, Plot.CAUSAL, "MT helping Jesse escape the train"),
    (16, 17, Plot.SERIAL, "Grace's gang"),
    (17, 18, Plot.SERIAL, "Reflection police attacking MT"),
    (17, 18, Plot.SERIAL, "Jesse gone"),
    (18, 19, Plot.SERIAL, "MT's plan to get a number"),
    (19, 20, Plot.SERIAL, "MT confronting One-One")]

show.foreshadowing = [
    (1, 5, Foreshadowing.MAJOR, "Conductor briefly flashes by in background when Tulip wakes up; Existence of the Conductor"),
    (3, 8, Foreshadowing.MAJOR, '''"I'll just keep your obituary on file then"; Atticus' death'''),
    (3, 10, Foreshadowing.MAJOR, "The Steward leaving after seeing One-One; One-One is the Conductor"),
    (6, 10, Foreshadowing.MAJOR, "One-One feeling the unfinished car is his fault; One-One is the Conductor"),
    (9, 10, Foreshadowing.MAJOR, "One-One able to easily control the memory tape; One-One is the Conductor"),
    (10, 16, Foreshadowing.MAJOR, "Grace in the passenger list"),
    (10, 17, Foreshadowing.MAJOR, "Simon in the passenger list")]
