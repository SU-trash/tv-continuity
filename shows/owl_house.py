#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import Show, Plot

'''Continuity data on the show The Owl House.'''

show = Show(
    title='The Owl House',
    brief_title='Owl House',
    seasons={1: dict(start=1, end=10, color='#FADA5E')},
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
        10: 'Escape of the Palisman'})

show.plot_threads = [
    (3, 5, Plot.CAUSAL, "Luz and Amity's relationship development"),
    (4, 5, Plot.REFERENTIAL, "Luz' light spell"),
    (4, 5, Plot.REFERENTIAL, "Eda's curse"),
    (4, 6, Plot.CAUSAL, "Eda's curse"),
    (5, 7, Plot.CAUSAL, "Luz and Amity's relationship development"),
    (5, 8, Plot.REFERENTIAL, "Eda & Lilith / Emperor's Coven"),
    (6, 10, Plot.CAUSAL, "Eda's Curse"),
    (7, 10, Plot.REFERENTIAL, "The Bat Queen and her children")]
