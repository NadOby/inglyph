#!/usr/bin/env python

import itertools

# Glyph have 11 dots
# TODO add illustration
dots = [1,2,3,4,5,6,7,8,9,10,11]

# Using sets cause it is easyer to maniipulate
# Here all the possible combinations of two dots e.g. strokes
comb_all = set(itertools.combinations(dots, 2))

# There are forbidden combinatios that are impossible in the game
comb_forbidden = set([(1,9),(1,10),(2,6),(2,8),(2,10),(3,5),(3,6),(3,7),(3,9),(2,11),(3,11),(1,11)])

comb_possible = comb_all - comb_forbidden
