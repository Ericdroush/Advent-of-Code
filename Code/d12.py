# -*- coding: utf-8 -*-
"""
Created on Sat Apr 2 

@author: ericdroush
"""
import numpy as np
import random
import pathfinding
import time

with open('../Input/d12_test.txt') as f:
    inp = f.readlines()


attempts = 100

#Initialize map
max_i = len(inp)
max_j = len(inp[1].strip())
elevation = np.zeros((max_i, max_j))

#Create the map from the input
for i in range(len(inp)):
    line = inp[i].strip()
    for j in range(len(line)):
        if line[j].islower():
            elevation[i,j] = ord(line[j])
        elif line[j] == 'S':
            elevation[i,j] = ord('a')
            start = [i, j]
        elif line[j] == 'E':
            elevation[i,j] = ord('z')
            end = [i, j]
            
print(elevation)
#Find paths
step = []
path = ['^', 'v', '<', '>']

t0 = time.perf_counter()

for attempt in range(attempts):
    end_found = False
    loci = start[0]
    locj = start[1]
    tracker = np.full((max_i, max_j), '.')
    tracker[loci, locj] = 'S'
    step.append(0)
    while not end_found:
        #Check all moves
        step[-1] += 1
        opt = np.array([0, 0, 0, 0])
        loci_new = [loci - 1, loci + 1, loci, loci]
        locj_new = [locj, locj, locj - 1, locj + 1] 
    
        #Check for viable moves
        for i in range(4):    
            if loci_new[i] >= 0 and loci_new[i] < max_i and locj_new[i] >= 0 and locj_new[i] < max_j:  
                if elevation[loci_new[i], locj_new[i]] <= elevation[loci, locj] + 1 and tracker[loci_new[i], locj_new[i]] == '.':
                    opt[i] = 1
        
        #If no moves left, start over
        if opt.sum() == 0:
            loci = start[0]
            locj = start[1]
            tracker = np.full((max_i, max_j), '.')
            tracker[loci, locj] = 'S'
            step[-1] = 0
        
        else: 
            opt2 = []
            for i in range(4):
                if opt[i] > 0:
                    #Need to check if any of the moves are the End
                    if loci_new[i] == end[0] and locj_new[i] == end[1]:
                        loci = loci_new[i]
                        locj = locj_new[i]
                        tracker[loci, locj] = 'E'
                        end_found = True
                        break                    
                    else:                    
                        opt2.append(i)
            
            if not end_found:
                i = random.choice(opt2)
                loci = loci_new[i]
                locj = locj_new[i]
                tracker[loci, locj] = path[i]
        
        #print(attempt, step[-1])
        #print(tracker)    

    print(attempt, step[-1])        
    print(tracker)  
    
    
print(step)   
print('The path with the least amount of steps was found in', min(step), 'steps') 
print('Run time = ', time.perf_counter() - t0)
    
    