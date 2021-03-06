#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show Rick and Morty.'''

show = Show(
    title='Rick and Morty',
    seasons={
        1: {'color': '#804060',
            'episodes': {
                'S1E1': 'Pilot',
                'S1E2': 'Lawnmower Dog',
                'S1E3': 'Anatomy Park',
                'S1E4': 'M. Night Shaym-Aliens!',
                'S1E5': 'Meeseeks and Destroy',
                'S1E6': 'Rick Potion #9',
                'S1E7': 'Raising Gazorpazorp',
                'S1E8': 'Rixty Minutes',
                'S1E9': 'Something Ricked This Way Comes',
                'S1E10': 'Close Rick-counters of the Rick Kind',
                'S1E11': 'Ricksy Business'}},
        2: {'color': '#804060',
            'episodes': {
                'S2E1': 'A Rickle in Time',
                'S2E2': 'Mortynight Run',
                'S2E3': 'Auto Erotic Assimilation',
                'S2E4': 'Total Rickall',
                'S2E5': 'Get Schwifty',
                'S2E6': 'The Ricks Must Be Crazy',
                'S2E7': 'Big Trouble in Little Sanchez',
                'S2E8': 'Interdimensional Cable 2: Tempting Fate',
                'S2E9': "Look Who's Purging Now",
                'S2E10': 'The Wedding Squanchers'}},
        3: {'color': '#804060',
            'episodes': {
                'S3E1': 'The Rickshank Rickdemption',
                'S3E2': 'Rickmancing the Stone',
                'S3E3': 'Pickle Rick',
                'S3E4': 'Vindicators 3: The Return of Worldender',
                'S3E5': 'The Whirly Dirly Conspiracy',
                'S3E6': 'Rest and Ricklaxation',
                'S3E7': 'The Ricklantis Mixup',
                'S3E8': "Morty's Mind Blowers",
                'S3E9': "The ABC's of Beth",
                'S3E10': 'The Rickchurian Mortydate'}},
        4: {'color': '#804060',
            'episodes': {
                'S4E1': 'Edge of Tomorty: Rick Die Rickpeat',
                'S4E2': 'The Old Man and the Seat',
                'S4E3': "One Crew over the Crewcoo's Morty",
                'S4E4': "Claw and Hoarder: Special Ricktim's Morty",
                'S4E5': 'Rattlestar Ricklactica',
                'S4E6': 'Never Ricking Morty',
                'S4E7': 'Promortyus',
                'S4E8': 'The Vat of Acid Episode',
                'S4E9': 'Childrick of Mort',
                'S4E10': 'Star Mort Rickturn of the Jerri'}}})

show.plot_threads = [
    ('S1E6', 'S1E8', Plot.REFERENTIAL, "Rick and Morty's bodies in the backyard"),
    ('S1E11', 'S2E1', Plot.CAUSAL, 'Unfreezing time after the party cleanup'),
    ('S1E11', 'S2E10', Plot.CAUSAL, "Tammy/Bird-Person's relationship"),
    ('S2E10', 'S3E1', Plot.SERIAL, 'Rick in the galactic prison'),
    ('S2E10', 'S3E1', Plot.CAUSAL, 'Tammy having killed Bird-Person'),
    ('S3E1', 'S3E2', Plot.CAUSAL, "Beth/Jerry's divorce"),
    ('S3E1', 'S3E5', Plot.CAUSAL, "Jerry's worsening self-esteem post-divorce"),
    ('S1E10', 'S3E7', Plot.CAUSAL, "Evil Morty's schemes"),
    ('S3E1', 'S3E9', Plot.CAUSAL, 'Jerry dating after the divorce'),
    ('S3E9', 'S3E10', Plot.CAUSAL, "Beth worrying about whether she's a clone"),
    ('S3E1', 'S3E10', Plot.CAUSAL, "Beth/Jerry's divorce"),
    ('S1E10', 'S4E6', Plot.REFERENTIAL, 'Evil Morty'),
    ('S3E1', 'S4E10', Plot.CAUSAL, 'Tammy and Bird-Person'),
    ('S3E3', 'S4E10', Plot.REFERENTIAL, 'The family therapy sessions'),
    ('S3E9', 'S4E10', Plot.CAUSAL, "Beth's clone")]
