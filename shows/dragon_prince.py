#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show The Dragon Prince.'''

show = Show(
    title='The Dragon Prince',
    brief_title='Dragon Prince',
    # Season colors / episode titles from https://en.wikipedia.org/wiki/The_Dragon_Prince#Episodes
    seasons={
        1: {'color': '#C8A2C8',
            'episodes': {
                'S1E1': 'Echoes of Thunder',
                'S1E2': 'What Is Done',
                'S1E3': 'Moonrise',
                'S1E4': 'Bloodthirsty',
                'S1E5': 'An Empty Throne',
                'S1E6': 'Through the Ice',
                'S1E7': 'The Dagger and the Wolf',
                'S1E8': 'Cursed Caldera',
                'S1E9': 'Wonderstorm'}},
        2: {'color': '#6DA1B3',
            'episodes': {
                'S2E1': 'A Secret and a Spark',
                'S2E2': 'Half Moon Lies',
                'S2E3': 'Smoke and Mirrors',
                'S2E4': 'Voyage of the Ruthless',
                'S2E5': 'Breaking the Seal',
                'S2E6': 'Heart of a Titan',
                'S2E7': 'Fire and Fury',
                'S2E8': 'The Book of Destiny',
                'S2E9': 'Breathe'}},
        3: {'color': '#E49D65',
            'episodes': {
                'S3E1': 'Sol Regem',
                'S3E2': 'The Crown',
                'S3E3': 'Ghost',
                'S3E4': 'The Midnight Desert',
                'S3E5': 'Heroes and Masterminds',
                'S3E6': 'Thunderfall',
                'S3E7': 'Hearts of Cinder',
                'S3E8': 'Dragonguard',
                'S3E9': 'The Final Battle'}}})

show.plot_threads = [
    ('S1E1', 'S1E2', Plot.CAUSAL, "Assassins / Rayla's disavowal"),
    ('S1E2', 'S1E3', Plot.CAUSAL, "Assassins / The discovery of the Dragon King's egg"),
    ('S1E3', 'S1E4', Plot.CAUSAL, "The gang's journey to return the Dragon Prince"),
    ('S1E3', 'S1E4', Plot.CAUSAL, "King Harrow's death"),
    ('S1E3', 'S1E5', Plot.CAUSAL, "The gang's journey to return the Dragon Prince"),
    ('S1E4', 'S1E5', Plot.CAUSAL, "Viren's reign"),
    ('S1E3', 'S1E6', Plot.CAUSAL, "The gang's journey to return the Dragon Prince"),
    ('S1E5', 'S1E6', Plot.CAUSAL, "Amaya's insistence on a search for the princes"),
    ('S1E6', 'S1E7', Plot.CAUSAL, "Claudia and Soren's search for the princes"),
    ('S1E6', 'S1E7', Plot.CAUSAL, "The egg's injury"),
    ('S1E3', 'S1E8', Plot.CAUSAL, "The captured Runaan"),
    ('S1E6', 'S1E8', Plot.CAUSAL, "The mystery of the magic mirror"),
    ('S1E7', 'S1E8', Plot.CAUSAL, "Search for the healer atop the Cursed Caldera"),
    ('S1E3', 'S1E9', Plot.REFERENTIAL, "Callum's stolen Primal Stone"),
    ('S1E6', 'S1E9', Plot.CAUSAL, "The mystery of the magic mirror"),
    ('S1E7', 'S1E9', Plot.CAUSAL, "Search for the healer atop the Cursed Caldera"),
    ('S1E7', 'S1E9', Plot.CAUSAL, "Claudia and Soren's search for the princes"),
    ('S1E4', 'S2E1', Plot.CAUSAL, "Viren's reign"),
    ('S1E5', 'S2E1', Plot.CAUSAL, "Amaya defending the breach"),
    ('S1E9', 'S2E1', Plot.CAUSAL, "The gang and Zym/Lujanne, loss of the Primal Stone"),
    ('S1E9', 'S2E1', Plot.CAUSAL, "Claudia and Soren having found the gang"),
    ('S1E3', 'S2E8', Plot.CAUSAL, "Rayla having hidden King Harrow's death from the princes"),
    ('S1E6', 'S2E2', Plot.CAUSAL, "The mystery of the magic mirror"),
    ('S2E1', 'S2E2', Plot.CAUSAL, "Rayla captured by Claudia/Soren"),
    ('S1E6', 'S1E7', Plot.CAUSAL, "Corvus tracking the gang"),
    ('S2E2', 'S2E3', Plot.CAUSAL, "The room in the mirror"),
    ('S2E2', 'S2E3', Plot.CAUSAL, "Callum having learned of Harrow's death / Claudia and Soren's machinations"),
    ('S1E3', 'S2E4', Plot.CAUSAL, "The gang's journey to return the Dragon Prince"),
    ('S2E1', 'S2E4', Plot.CAUSAL, "The sunfire elves' attack on the breach/Amaya"),
    ('S2E1', 'S2E4', Plot.REFERENTIAL, "Viren having called for a Pentarchy"),
    ('S2E1', 'S2E4', Plot.CAUSAL, "Lujanne having told Callum about Arcanums"),
    ('S2E3', 'S2E4', Plot.CAUSAL, "Viren and the elf in the mirror"),
    ('S2E1', 'S2E5', Plot.CAUSAL, "Viren having called for a Pentarchy"),
    ('S2E3', 'S2E5', Plot.CAUSAL, "Harrow's letter to Callum"),
    ('S2E5', 'S2E6', Plot.SERIAL, "Continuation of Viren's story about the titan"),
    ('S2E5', 'S2E6', Plot.SERIAL, "Callum reading Harrow's letter to him"),
    ('S1E4', 'S2E6', Plot.REFERENTIAL, "The primal magic cube Callum retrieved from the lodge"),
    ('S2E1', 'S2E7', Plot.CAUSAL, "Viren having used the king's seal to call for a Pentarchy"),
    ('S2E3', 'S2E7', Plot.CAUSAL, "Corvus having been captured by Claudia and Soren"),
    ('S2E4', 'S2E7', Plot.CAUSAL, "Viren and the elf in the mirror's spell"),
    ('S1E3', 'S2E8', Plot.CAUSAL, "Rayla having hidden King Harrow's death from the princes"),
    ('S1E6', 'S2E8', Plot.REFERENTIAL, "Viren's order to Soren to kill the princes"),
    ('S2E7', 'S2E8', Plot.CAUSAL, "Callum's sickness after using dark magic, Corvus freed"),
    ('S2E7', 'S2E8', Plot.CAUSAL, "Soren's injured spine"),
    ('S2E7', 'S2E8', Plot.CAUSAL, "Viren able to speak with Aaravos"),
    ('S1E3', 'S2E9', Plot.CAUSAL, "The gang's journey to return the Dragon Prince"),
    ('S2E4', 'S2E9', Plot.CAUSAL, "Callum's efforts to learn the Sky Arcanum"),
    ('S2E8', 'S2E9', Plot.CAUSAL, "Ezran and Claudia mulling over their problems"),
    ('S2E7', 'S2E9', Plot.CAUSAL, "Callum's sickness after using dark magic"),
    ('S2E7', 'S2E9', Plot.CAUSAL, "Viren able to speak with Aaravos"),
    ('S2E8', 'S2E9', Plot.CAUSAL, "Claudia's determination to heal Soren"),
    ('S2E8', 'S2E9', Plot.CAUSAL, "Ezran learning of Harrow's death and that he is king now"),
    ('S1E3', 'S3E1', Plot.CAUSAL, "Callum/Rayla's journey to return the Dragon Prince"),
    ('S2E4', 'S3E1', Plot.CAUSAL, "Amaya/the garrison unable to defend the breach from the sunfire elves"),
    ('S2E9', 'S3E1', Plot.REFERENTIAL, "Callum having learned the Sky Arcanum"),
    ('S2E9', 'S3E1', Plot.REFERENTIAL, "Gren freed"),
    ('S2E9', 'S3E1', Plot.CAUSAL, "Ezran taking up the kingship"),
    ('S1E3', 'S3E2', Plot.CAUSAL, "Callum/Rayla's journey to return the Dragon Prince"),
    ('S1E6', 'S3E2', Plot.CAUSAL, "Claudia and Soren's orders from Viren"),
    ('S2E5', 'S3E2', Plot.CAUSAL, "Viren's call for war with Xadia"),
    ('S2E9', 'S3E2', Plot.CAUSAL, "Ezran taking up the kingship"),
    ('S2E9', 'S3E2', Plot.CAUSAL, "Viren/Aaravos' magic assassins"),
    ('S1E3', 'S3E3', Plot.CAUSAL, "Rayla's abandonment of her mission"),
    ('S1E6', 'S3E3', Plot.CAUSAL, "Claudia and Soren's orders from Viren"),
    ('S3E1', 'S3E3', Plot.CAUSAL, "Amaya captured by the Sunfire Elves"),
    ('S3E2', 'S3E3', Plot.CAUSAL, "Prince Kasef's dissatisfaction with Ezran's refusal to go to war"),
    ('S1E3', 'S3E4', Plot.CAUSAL, "Callum/Rayla's journey to return the Dragon Prince"),
    ('S3E3', 'S3E4', Plot.CAUSAL, "Ethari's message to the Dragon Queen informing her of Zym"),
    ('S3E3', 'S3E4', Plot.CAUSAL, "Kasef/Saleer's plot against Ezran"),
    ('S2E7', 'S3E4', Plot.CAUSAL, "Aaravos' growing hold on Viren"),
    ('S1E9', 'S3E5', Plot.REFERENTIAL, "Lujanne's assistance"),
    ('S3E3', 'S3E5', Plot.CAUSAL, "Soren's disillusionment with Viren"),
    ('S3E4', 'S3E5', Plot.CAUSAL, "Zym stolen by Nyx / Callum/Rayla's kiss"),
    ('S3E4', 'S3E5', Plot.CAUSAL, "Ezran imprisoned"),
    ('S2E6', 'S3E6', Plot.CAUSAL, "Avizandum having killed Sarai"),
    ('S3E1', 'S3E6', Plot.REFERENTIAL, "The bridge across the Breach having been destroyed"),
    ('S3E5', 'S3E6', Plot.CAUSAL, "Viren's march on Xadia"),
    ('S3E5', 'S3E6', Plot.CAUSAL, "Ezran's escape and journey to rejoin Callum/Rayla"),
    ('S1E3', 'S3E7', Plot.CAUSAL, "Callum/Rayla's journey to return the Dragon Prince"),
    ('S2E7', 'S3E7', Plot.CAUSAL, "The dragon Pyrrah the gang rescued"),
    ('S3E1', 'S3E7', Plot.CAUSAL, "Amaya captured by the Sunfire Elves"),
    ('S3E3', 'S3E7', Plot.CAUSAL, "Soren's disillusionment with Viren"),
    ('S3E5', 'S3E7', Plot.CAUSAL, "Viren's march on Xadia"),
    ('S3E5', 'S3E7', Plot.REFERENTIAL, "Callum/Rayla's romantic relationship"),
    ('S1E3', 'S3E8', Plot.CAUSAL, "The gang's journey to return the Dragon Prince"),
    ('S3E6', 'S3E8', Plot.CAUSAL, "Continuation of the story of Viren stealing the Dragon Prince's egg"),
    ('S3E8', 'S1E2', Plot.CAUSAL, "The stolen dragon king/queen's egg"),
    ('S3E7', 'S3E8', Plot.CAUSAL, "Soren betraying Viren to warn the protagonists of the army"),
    ('S3E7', 'S3E8', Plot.CAUSAL, "Amaya and the surviving Sunfire Elves"),
    ('S3E5', 'S3E9', Plot.REFERENTIAL, "Callum/Rayla's romantic relationship"),
    ('S3E8', 'S3E9', Plot.CAUSAL, "The protagonists' decision to stay and fight Viren and his army"),
    ('S3E8', 'S3E9', Plot.REFERENTIAL, "The flight spell")]
