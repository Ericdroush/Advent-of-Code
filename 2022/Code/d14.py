# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 2023

@author: ericd
"""
import numpy as np

with open('../Input/d14_input.txt') as f:
    inp = f.readlines()
    inp = [x.strip() for x in inp]

#Process input
xpts = []
ypts = []

for line in inp:
    xpt = []
    ypt = []
    for pts in line.split(' -> '):
        xpt.append(int(pts.split(',')[0])) 
        ypt.append(int(pts.split(',')[1])) 
    xpts.append(xpt)
    ypts.append(ypt)

#Initialize Cave
ymax = max(max(x) for x in ypts)
xmin = min(min(x) for x in xpts)
xmax = max(max(x) for x in xpts)

has_floor = True   #False for part 1, True for part 2
if has_floor:
    xmax += 200
    xpts.append([0, xmax])
    ymax += 2
    ypts.append([ymax, ymax])
    cave = np.full((ymax + 1, xmax + 1),'.')
else:
    cave = np.full((ymax + 2, xmax + 2),'.')
print('ymax =', ymax, 'xmin =', xmin, 'xmax =', xmax)

#Initialize Rock
for i in range(len(xpts)):
    for j in range(len(xpts[i])):
        cave[ypts[i][j], xpts[i][j]] = '#'
        if j + 1 != len(xpts[i]):  #Connect the points
            if xpts[i][j] == xpts[i][j + 1]:
                if ypts[i][j + 1] > ypts[i][j]:
                    step = 1
                else:
                    step = -1
                for k in range(ypts[i][j], ypts[i][j + 1], step):
                    cave[k, xpts[i][j]] = '#'
            else:
                if xpts[i][j + 1] > xpts[i][j]:
                    step = 1
                else:
                    step = -1
                for k in range(xpts[i][j],xpts[i][j + 1], step):
                    cave[ypts[i][j], k] = '#'
                    

cave[0, 500]= '+'
#print('done building cave')
#print(cave[0:ymax + 2, xmin - 1:xmax + 2])
drop_sand = True
is_falling = True
sand = 0
while drop_sand:
    #Beging drop    
    xpos = 500
    ypos = 0
    sand += 1
    is_falling = True
    while is_falling:
        if cave[ypos + 1, xpos] == '.':
            ypos += 1
        elif cave[ypos + 1, xpos - 1] == '.':
            xpos -= 1
            ypos += 1
        elif cave[ypos + 1, xpos + 1] == '.':
            xpos += 1
            ypos += 1
        else:
            cave[ypos, xpos] = 'o'
            is_falling = False
            if ypos == 0:
                drop_sand = False
        if ypos == ymax:   #Abyss reached
            drop_sand = False
            is_falling = False
            sand -= 1    #Remove the last unit of sand that fell into the abyss
        
print(cave[0:ymax + 2, xmin - 1:xmax + 2])
print(sand, ' units of sand were stacked up')