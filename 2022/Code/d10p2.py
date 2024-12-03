# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:30:20 2022

This code gives the right answer to part 2, but no longer gives the right answer to part 1

It should give 14560 for the first part
@author: ericd
"""

with open('../Input/d10_input.txt') as f:
    inp = f.readlines()

xreg = [1]
xadd = 0
x = -1

disp = ''
row = ''

for line in inp:
    x += 1
    #print(len(xreg), x)
    if x == 39:
        x = -1
        disp = disp + row + '\n'  
        row = ''
    else:
        if xreg[-1] >= x - 1 and xreg[-1] <= x + 1:    
            row = row + '#'
        else:
            row = row + '.'
    xreg.append(xadd + xreg[-1])

    if line[0] == 'n':
        xadd = 0
    else:
        x += 1
        #print(len(xreg), x)
        if x == 39:
            x = -1
            disp = disp + row + '\n'  
            row = ''
        else:
            if xreg[-1] >= x - 1 and xreg[-1] <= x + 1:    
                row = row + '#'
            else:
                row = row + '.'
    
        xadd = int(line.strip().split()[1])
        xreg.append(xadd + xreg[-1])
        xadd = 0

xadd = 0
cycle_check = [20, 60, 100, 140, 180, 220]
for cycle in cycle_check:
    xadd += xreg[cycle] * cycle
    print(cycle, ' cycle, x = ', xreg[cycle], ' and strength = ', xreg[cycle] * cycle)

print('The sum of the signal strengths is ', xadd)
print()
print(disp)