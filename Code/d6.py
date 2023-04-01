# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 19:20:53 2022

@author: ericd
"""

with open('../Input/d6_input.txt') as f:
    data = f.read()

for x in range(13,len(data)):
    sop = True
    print('x = ', x)
    print(data[x - 13:x + 1])
    for i in range(x-13,x+1):
        print(i, data[i])
        if data[x - 13:x + 1].count(data[i]) > 1:
            sop = False
    if sop:
        print('First character after ', x + 1)   #+1 to convert from 0 base to human counting
        print('Total Characters ', len(data))
        break;
    
        
        
        