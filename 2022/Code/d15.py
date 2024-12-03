# -*- coding: utf-8 -*-
"""
Created on Sat May 13 2023

@author: ericd
"""
import numpy as np
import time

t0 = time.perf_counter_ns()

with open('../Input/d15_input.txt') as f:
    inp = [x.strip() for x in f.readlines()]
    
#Process input
sx, sy, bx, by, dist = [], [], [], [], []

for line in inp:
    values = line.split(',')
    sx.append(int(values[0].split('=')[1]))
    sy.append(int(values[1].split('=')[1].split(':')[0]))
    bx.append(int(values[1].split('=')[2]))
    by.append(int(values[2].split('=')[1]))
    dist.append(abs(sx[-1] - bx[-1]) + abs(sy[-1] - by[-1]))

#    sx.append(int(line.split(',')[0].split('=')[1]))
#    sy.append(int(line.split(':')[0].split('=')[2]))
#    bx.append(int(line.split(',')[1].split('=')[2]))
#    by.append(int(line.split(',')[2].split('=')[1]))
#    dist.append(abs(sx[-1] - bx[-1]) + abs(sy[-1] - by[-1]))

ymin = min(min(sy),min(by))
ymax = max(max(sy),max(by)) 
xmin = min(min(sx),min(bx))
xmax = max(max(sx),max(bx)) 
dmax = max(dist)

print('Number of sensor pairs = ', len(sx))
print('ymin =', ymin, 'ymax =', ymax, 'xmin =', xmin, 'xmax =', xmax)
print('time = ', f'{(time.perf_counter_ns() - t0)/100000000:0f}')

yo = 2000000 #row of interest
no_beacon = 0

if False:
    for x in range(xmin - dmax, xmax + dmax): 
        for i in range(len(sx)):
            if by[i] == yo and bx[i] == x:
                break
            di = abs(sx[i] - x) + abs(sy[i] - yo)
            if di <= dist[i]:
                no_beacon += 1
                break 

if True:
    t0 = time.perf_counter_ns()
    edge = set()
    redux_edge = set()
    x, y = [0] * 4, [0] * 4
    
    for loop in range(4):
        edge = set()
        for i in range(len(sx)):   #len(sx)
            t1 = time.perf_counter_ns()
            print('Loop:', loop, 'Set:', i, 'Distance =', dist[i])
            for d in range(dist[i] + 2):   #dist[i] + 2    #Build list of edge coordinates
                x[0] = x[1] = sx[i] + d
                x[2] = x[3] = sx[i] - d
                y[0] = y[2] = sy[i] + (dist[i] - d + 1 )
                y[1] = y[3] = sy[i] - (dist[i] - d + 1 )
                for j in range(4):
                    if 1000000 * loop <= x[j] <= 1000000 * (loop + 1) and 0 <= y[j] <= 4000000:               
                        edge.add((x[j], y[j]))
                        if (x[j], y[j]) in edge:
                            true_point = True
                            for k in range(len(sx)):
                                if k != i:
                                    if (abs(x[j] - sx[k]) + abs(y[j] - sy[k])) <= dist[k]:
                                        true_point = False
                                        break
                            if true_point:
                                redux_edge.add((x[j], y[j]))
    
            print('There are ', len(edge), 'edge points.  But only ', len(redux_edge), 'redueced points.')
            #print('set time = ', f'{(time.perf_counter_ns() - t1)/100000000:0f}')
        
        print('There are ', len(edge), 'edge points.  But only ', len(redux_edge), 'redueced points.')
        print('set time = ', f'{(time.perf_counter_ns() - t0)/100000000:0f}')
        del edge

    if len(redux_edge) == 1:
        pt = redux_edge.pop()
        tune_freq = 4000000 * pt[0] + pt[1]
        print('The edge point is x =', pt[0], ', y =', pt[1], ', and the tuning frequency is', tune_freq)

if False: #This is the loop I'm messing with
    np.set_printoptions(linewidth=200)
    for offset in range (1, 5):
        cave = np.full((100, 4000000),0)
        #Populate Space
        for i in range(len(sx)):
            print(i)
            dist = abs(sx[i] - bx[i]) + abs(sy[i] - by[i])
            for xadd in range(-dist,dist + 1):
                for yadd in range(-dist,dist + 1):
                    if abs(xadd) + abs(yadd) <= dist:
                        if sy[i] + yadd <= ymax and sy[i] + yadd >= 0 and sx[i] + xadd <= xmax and sx[i] + xadd >= 0:  
                            cave[sy[i] + yadd, sx[i] + xadd] = 1        
        #        if sx[i] >= 0:
        #            cave[sy[i], sx[i]] = 'S'
        #        if bx[i] >= 0:
        #            cave[by[i], bx[i]] = 'B'    
        #        print(sy[i], sx[i], by[i], bx[i], dist)
        #        print(np.array2string(cave, separator = '').replace("'",''))
        cave2 = cave[0:20,0:20]
        row_min = np.min(cave2, axis = 0).argmin()
        col_min = np.min(cave2, axis = 1).argmin()
        print(col_min, row_min, row_min * 4000000 + col_min)
    
    
    
#    print(np.array2string(cave[0:20,0:20], separator = '').replace("'",''))


if False:  #This loop works for part 1 despite some flaws
    cave = np.zeros((ymax + 1, xmax + 1))
    #Populate Space
    for i in range(len(sx)):
        dist = abs(sx[i] - bx[i]) + abs(sy[i] - by[i])
        for xadd in range(-dist,dist):
            for yadd in range(-dist,dist):
                if xadd + yadd <= dist and sy[i]:
                    if sy[i] + yadd <= ymax and sy[i] - yadd >= ymin and sx[i] + xadd <= xmax and sx[i] - xadd >= xmin:  
                        cave[sy[i] + yadd, sx[i] + xadd] = 1        

    np.set_printoptions(linewidth=200)
    print(np.array2string(cave, separator = ''))

    no_beacon = np.sum(cave[10])

    print('There are ', no_beacon, "spots where a beacon ain't")
#7086311 - too high
#5658320 - STILL TOO HIGH
#5127797 - Right answer for part 1