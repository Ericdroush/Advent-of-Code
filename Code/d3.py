# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:20:22 2022

@author: ericd
"""


with open('../Input/d3_input.txt') as f:
    lines = f.readlines()

p_list = 'abcdefghijklmnopqrstuvwxyz'
psum = 0
bsum = 0
count = 1
for l in range(len(lines)):
    line = lines[l].strip()
    for x in line[0:int((len(line)/2))]:
        if x in line[int(len(line)/2): len(line)+1]:
            if x in p_list:
                priority = p_list.index(x) + 1   
            else: 
                priority = p_list.index(x.lower()) + 27
            psum = psum + priority
            break;
    if count == 3:
        count = 1
        for x in line:
            if x in lines[l - 1] and x in lines[l - 2]:
                if x in p_list:
                    badge_priority = p_list.index(x) + 1   
                else: 
                    badge_priority = p_list.index(x.lower()) + 27
                print(x, badge_priority)
                bsum = bsum + badge_priority
                break;
    else:
        count += 1

print('The total priority is ', psum)
print('The badge priority is ', bsum)