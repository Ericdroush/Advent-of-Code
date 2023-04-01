# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:29:30 2022

@author: ericd
"""

with open('../Input/d4_input.txt') as f:
    lines = f.readlines()

redundant = 0
overlapped = 0
not_overlapped= 0
print('Number of lines ', len(lines))

for line in lines:
    line = line.strip()
    e1 = int(line.split(',')[0].split('-')[0])
    e2 = int(line.split(',')[0].split('-')[1])
    e3 = int(line.split(',')[1].split('-')[0])
    e4 = int(line.split(',')[1].split('-')[1])
    
    if (e1 >= e3 and e2 <= e4) or (e3 >= e1 and e4 <= e2):
        #print(e1, e2, e3, e4, '**')
        redundant += 1

    if e1 > e4 or e2 < e3:
        print(e1, e2, e3, e4)
        not_overlapped += 1
    else:
        overlapped += 1
        print(e1, e2, e3, e4, 'O')

        
print('The number of redundant pairings is ', redundant)
print('The number of overlapped pairings is ', overlapped)
        