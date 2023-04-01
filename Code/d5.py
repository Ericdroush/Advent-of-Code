# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 18:05:31 2022

@author: ericd
"""
stacks = {
        '1': ['D', 'L', 'V', 'T', 'M', 'H', 'F'],
        '2': ['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P'],
        '3': ['R', 'S', 'D', 'M', 'P', 'H'],
        '4': ['L', 'B', 'V', 'F'],
        '5': ['N', 'H', 'G', 'L', 'Q'],
        '6': ['W', 'B', 'D', 'G', 'R', 'M', 'P'],
        '7': ['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q'],
        '8': ['C', 'L', 'W'],
        '9': ['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T']
        }
CrateMover = 9001

with open('../Input/d5_input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    
    count = int(line.split()[1])
    from_stack = line.split()[3]
    to_stack = line.split()[5]
    if CrateMover == 9000:
        for i in range(count):
            stacks[to_stack].append(stacks[from_stack][-1])
            stacks[from_stack].pop()
    elif CrateMover == 9001:
        print(count, from_stack, to_stack)
        print(stacks[from_stack])
        print(stacks[to_stack])
        stacks[to_stack].extend(stacks[from_stack][-count:])
        stacks[from_stack] = stacks[from_stack][:-count] 
        print(stacks[from_stack])
        print(stacks[to_stack])

code = ''        
for i in range(1,10):
    code = code + stacks[str(i)][-1]
        

print('The final top block is ', code)    

