# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:30:20 2022

@author: ericd
"""

with open('../Input/d10_input.txt') as f:
    inp = f.readlines()

xreg = [1]
xadd = 0
x = 0

disp = ''
row = ''

for line in inp:
    x += 1
    print(len(xreg), x)
    if x == 40:
        x = 0
        disp = disp + row + '\n'  
        row = ''
    if x >= xreg[-1] - 1 and x <= xreg[-1] + 1:    
        row = row + '#'
    else:
        row = row + '.'
    xreg.append(xadd + xreg[-1])

    if line[0] == 'n':
        xadd = 0
    else:
        x += 1
        print(len(xreg), x)
        if x == 40:
            x = 0
            disp = disp + row + '\n'  
            row = ''
        if x >= xreg[-1] - 1 and x <= xreg[-1] + 1:    
            row = row + '#'
        else:
            row = row + '.'
    
        xadd = int(line.strip().split()[1])
        xreg.append(xreg[-1])
        

xadd = 0
cycle_check = [20, 60, 100, 140, 180, 220]
for cycle in cycle_check:
    xadd += xreg[cycle] * cycle
    print(cycle, ' cycle, x = ', xreg[cycle], ' and strength = ', xreg[cycle] * cycle)

print('The sum of the signal strengths is ', xadd)
print()
print(disp)