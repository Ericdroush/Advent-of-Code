# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 08:28:28 2023

@author: ericd
"""
from copy import deepcopy

with open('../Input/d13_input.txt') as f:
    inp = f.readlines()
    inp = [x.strip() for x in inp]


def comp(left_in, right_in):

    while len(left_in) > 0 and len(right_in) > 0: 
        left = left_in.pop(0)
        right = right_in.pop(0)
        
        if type(left) == list and type(right) == list:
            order = comp(left, right)
            if order != 'T':
                return order
        elif type(left) == int and type(right) == int:
            if left > right:
                return 'L'
            if left < right:
                return 'R'
        elif type(left) == int :
            order = comp([left], right)
            if order != 'T':
                return order
        elif type(right) == int :
            order = comp(left, [right])
            if order != 'T':
                return order
            
    if len(left_in) > len(right_in):
        return 'L'
    elif len(left_in) < len(right_in):
        return 'R'
    else:
        return 'T'

#Read in the lines
l_list = []
r_list = []
for line in range(0, len(inp), 3):
    l_list.append(eval(inp[line]))
    r_list.append(eval(inp[line + 1]))
    
#For part 2
full = [[2]] + deepcopy(l_list + r_list) + [[6]] 
print(len(full))

#Determine if lines are in the proper order
ord_count = 0
pair_sum = 0
pair = 0
for pair in range(len(l_list)):
    
    order = comp(l_list[pair], r_list[pair])
                    
    if order == 'R':
        ord_count += 1
        pair_sum += pair + 1
        
    #print('Pair', pair, order)
    
print('The number of properly ordered lines is', ord_count, 'the sum of them is', pair_sum)
  
sort_list = []
i = 1
i_min = 0 
print(full[0])
while len(full) > 1:
    #print('imin', i_min, 'i', i)
    #print(full2[i_min], full2[i])
    full2 = deepcopy(full)
    order = comp(full2[i_min], full2[i])
    #print('order', order)
    #print('-------------------------------')
    if order == 'L':
        i_min = i   #new min found, update i_min
    if i == len(full) - 1: #made it to the end, the min is the min of the whole list
        sort_list.append(full.pop(i_min))
        full2 = deepcopy(full)
        i_min = 0
        i = 1
    else:
        i += 1
        
sort_list.append(full.pop(0))  #Add the last line remaining from full list, can't do this in the loop since there's nothing to compare it to

ds1 = 1 + sort_list.index([2]) 
ds2 = 1 + sort_list.index([6])
print(sort_list)
print('The distress packets are in location', ds1, 'and', ds2)
print('The decoder key is', ds1 * ds2)