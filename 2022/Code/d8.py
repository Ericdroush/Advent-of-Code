# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:30:20 2022

@author: ericd
"""
import numpy as np

with open('../Input/d8_input.txt') as f:
    trees = f.readlines()



cols = len(trees[0].strip())  #j
rows = len(trees)             #i

height = np.zeros((cols, rows))
for i in range(0, rows):
    for j in range(0, cols):
        height[i, j] = trees[i][j]

visible = np.zeros((cols, rows))

for i in range(0, rows):
    for j in range(0, cols):       
        #Set perimeter
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            visible[i, j] = 1
        else:
            if height[i, j] > height[i, 0:j].max():  #Left check
                visible[i, j] = 1
            if height[i, j] > height[i, j + 1:cols].max():  #Right check
                visible[i, j] = 1
            if height[i, j] > height[0:i, j].max():  #Top check
                visible[i, j] = 1
            if height[i, j] > height[i + 1:rows, j].max():  #Bottom check
                visible[i, j] = 1

np.set_printoptions(edgeitems = 10)
print(visible)
print('Total number of trees = ', rows * cols)
print('Number of visible trees = ', visible.sum())

#Part 2
scenic = np.zeros((cols, rows))

for i in range(0, rows):
    for j in range(0, cols):       
        #Left check
        count_left = 0
        if j != 0:
            for j2 in range(j - 1, -1, -1):
                if height[i,j2] < height[i,j]:
                    count_left += 1
                else:
                    count_left += 1
                    break
        #Right check
        count_right = 0
        if j != cols - 1:
            for j2 in range(j + 1, cols):
                if height[i,j2] < height[i,j]:
                    count_right += 1
                else:
                    count_right += 1
                    break
        #Top check
        count_top = 0
        if i != 0:
            for i2 in range(i - 1, -1, -1):
                if height[i2,j] < height[i,j]:
                    count_top += 1
                else:
                    count_top += 1
                    break
        #Bottom check
        count_bot = 0
        if i != rows - 1:
            for i2 in range(i + 1, rows):
                if height[i2,j] < height[i,j]:
                    count_bot += 1
                else:
                    count_bot += 1
                    break

        print('Counts: ', count_left, count_right, count_top, count_bot)
        scenic[i,j] = count_left * count_right * count_top * count_bot
        
np.set_printoptions(edgeitems = 6)
print(scenic)
print('The max scenic score is ', scenic.max())        