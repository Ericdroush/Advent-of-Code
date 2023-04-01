# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

with open('../Input/input.txt') as f:
    lines = f.readlines()
    
elf = []   
cal = 0
for line in lines:
    if len(line) == 1:
        elf.append(cal)
        cal = 0
    else:
        cal = cal + int(line.strip())
        
print('The number of elves is ', len(elf))
max_index = elf.index(max(elf))
max_cals = max(elf)
total_cals = max_cals

print('The elf with the highest number of calories is ', max_index)
print('The number of calories is ', max_cals)

elf[max_index] = 0
max_index = elf.index(max(elf))
max_cals = max(elf)
total_cals = total_cals + max_cals

print('The elf with the 2nd highest number of calories is ', max_index)
print('The number of calories is ', max_cals)

elf[max_index] = 0
max_index = elf.index(max(elf))
max_cals = max(elf)
total_cals = total_cals + max_cals

print('The elf with the 3rd highest number of calories is ', max_index)
print('The number of calories is ', max_cals)
print('The total number of calories for the top three elves is ', total_cals)
