#!/usr/bin/env python

import itertools
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Glyph have 11 dots
dots = [1,2,3,4,5,6,7,8,9,10,11]

# They are positioned in a gexagram (sort of).
pos = {1:(4,8),2:(0,6),3:(8,6),4:(2,5),5:(6,5),6:(4,4),7:(2,3),8:(6,3),9:(0,2),10:(8,2),11:(4,0)}

# Using sets because they are easier to manipulate
# Here all the possible combinations of two dots e.g. strokes
comb_all = set(itertools.combinations(dots, 2))

# There are forbidden strokes that are impossible in the game e.g you'll need to skip dot to draw it.
# Found empirically, not elegant but who cares.
comb_forbidden = set([(1,9),(1,10),(2,6),(2,8),(2,10),(3,5),(3,6),(3,7),(3,9),(2,11),(3,11),(1,11)])

# Lets enumerate edges exists are difference
comb_possible = comb_all - comb_forbidden

# Lets create graph using networkx module.
G=nx.Graph()

# And fill it with nodes and edges we have.
G.add_nodes_from (dots)
G.add_edges_from(comb_possible)

# Draw it just to see tha everything is OK.
nx.draw(G,pos)
plt.show()

# Adjacency matrix of the graph
summ=0
mat = nx.to_numpy_matrix(G)
for i in dots[1:]:
    paths = np.sum(np.linalg.matrix_power(mat, i))
    print ("number of path of lenght {} is {}".format(i, paths))
    summ +=paths

print ("sum of all the possible paths is {}".format(summ))
