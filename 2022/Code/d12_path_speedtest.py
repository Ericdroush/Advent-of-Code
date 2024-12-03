# -*- coding: utf-8 -*-
"""
Created on Sat Apr 2 
Requires pathfinding_er to be installed
Pathfinding_er is a modified version of the pathfinding module
Changes were made to the grid.py file, in the neighbors function to include a check 
    on height (height is captured in the variable weight)
    If the height is more than one greater than the current node, the node is no
    included as a neighbor

@author: ericdroush
"""

import numpy as np
from pathfinding_er.core.diagonal_movement import DiagonalMovement
from pathfinding_er.core.grid import Grid
from pathfinding_er.finder.a_star import AStarFinder
from pathfinding_er.finder.best_first import BestFirst
import time

with open('../Input/d12_input.txt') as f:
    inp = f.readlines()

#Initialize map
max_i = len(inp)
max_j = len(inp[1].strip())
elevation = np.zeros((max_i, max_j))
start_list = []
#Create the map from the input
for i in range(len(inp)):
    line = inp[i].strip()
    for j in range(len(line)):
        if line[j].islower():
            elevation[i, j] = ord(line[j])
            if line[j] == 'a':
                start_list.append([i, j])
        elif line[j] == 'S':
            elevation[i, j] = ord('a')
            start_loc = [i, j]
            start_list.append([i, j])
        elif line[j] == 'E':
            elevation[i, j] = ord('z')
            end_loc = [i, j]
            
print('matrix')
print(elevation)
print(max_i, max_j)
print('start', start_loc[0], start_loc[1])
print('end', end_loc[0], end_loc[1])

#Find paths
t0 = time.perf_counter()

grid = Grid(matrix = elevation)
start = grid.node(start_loc[1], start_loc[0])
end = grid.node(end_loc[1], end_loc[0])   

finder = AStarFinder(diagonal_movement=DiagonalMovement.never, weight = True)
path, runs = finder.find_path(start, end, grid)

#print('Details from true start - part 1')
print('AstarFinder')
print('operations:', runs, 'path length:', len(path) - 1)
print('Run time = ', time.perf_counter() - t0)

t0 = time.perf_counter()
grid = Grid(matrix = elevation)
start = grid.node(start_loc[1], start_loc[0])
end = grid.node(end_loc[1], end_loc[0])   
finder = BestFirst(diagonal_movement=DiagonalMovement.never, weight = True)
path, runs = finder.find_path(start, end, grid)
print('BiAstarFinder')
print('operations:', runs, 'path length:', len(path) - 1)
print('Run time = ', time.perf_counter() - t0)



#run_list = []
#print('Number of viable starting places', len(start_list))
#for s in start_list:
#    grid = Grid(matrix = elevation)
#    start = grid.node(s[1], s[0])
#    end = grid.node(end_loc[1], end_loc[0])   
#    
#    finder = AStarFinder(diagonal_movement=DiagonalMovement.never, weight = True)
#    path, runs = finder.find_path(start, end, grid)
#    #print('operations:', runs, 'path length:', len(path) - 1)
#    if len(path) > 0:
#        run_list.append(len(path) - 1)

#print('The shortest path from any a location is', min(run_list))
#print('operations:', runs, 'path length:', len(path) - 1)
#print(grid.grid_str(path=path, start=start, end=end)) 

#print('Run time = ', time.perf_counter() - t0)
    
    