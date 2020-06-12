#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Continuity data on the show The Owl House.'''

show = Show(
    title='The Owl House',
    brief_title='Owl House',
    seasons={1: dict(num_eps=20, color='#FADA5E')},
    episodes={
        1: 'A Lying Witch and a Warden',
        2: 'Witches Before Wizards',
        3: 'I Was a Teenage Abomination',
        4: 'The Intruder',
        5: 'Covention',
        6: "Hooty's Moving Hassle",
        7: 'Lost in Language',
        8: 'Once Upon a Swap',
        9: 'Something Ventured, Someone Framed',
        10: 'Escape of the Palisman',
        11: 'Adventures in the Elements'})

show.plot_threads = [
    # Ep 1 is technically causal to every episode of the show but doesn't matter for our seriality metric (by design)
    (1, 4, Plot.CAUSAL, "Luz entering the Boiling Isles and becoming Eda's apprentice"),
    (3, 5, Plot.REFERENTIAL, "Luz and Amity's rivalry"),
    (4, 5, Plot.REFERENTIAL, "Luz' light spell"),
    (4, 5, Plot.REFERENTIAL, "Eda's curse"),
    (4, 6, Plot.CAUSAL, "Eda's curse"),
    (5, 7, Plot.CAUSAL, "Luz and Amity's relationship development"),
    (5, 8, Plot.REFERENTIAL, "Eda and Lilith / Emperor's Coven"),
    (3, 9, Plot.CAUSAL, "Luz wanting to enrol in Hexside / heightened Hexside security"),
    (4, 10, Plot.CAUSAL, "Eda's Curse"),
    (7, 10, Plot.REFERENTIAL, "The Bat Queen and her children"),
    (7, 11, Plot.REFERENTIAL, "Luz/Amity's friendship, Emira & Edric making up for the library incident"),
    (9, 11, Plot.CAUSAL, "Luz preparing to go to Hexside")]
