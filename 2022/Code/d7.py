# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:30:20 2022

@author: ericd
"""

import pandas as pd
import copy

files = pd.DataFrame(columns = ['dir', 'file', 'size'])

with open('../Input/d7_input.txt') as f:
    lines = f.readlines()

cwd = {}
wd_path = []
for x in range(len(lines)):
    line = lines[x].strip()
    if '$ cd ..' in line:
        wd_path = wd_path[:-1]
        wd = '/'.join(wd_path)
    elif '$ cd' in line:
        wd_path.append(line.split()[-1])
        wd = '/'.join(wd_path)
        cwd[wd] = []
    elif '$ ls' in line:
        line = '' #set up while loop
        while (not '$' in line) and (x < (len(lines) - 1)):
            x += 1
            line = lines[x].strip()
            if line[0].isnumeric():
                sz = int(line.split()[0])
                fl = line.split()[1]
                files.loc[len(files.index)] = [wd, fl, sz] 
            elif 'dir' in line:
                cwd[wd].append(wd + '/' + line.split()[1])
        x -= 1


#Fill out directories with all subdirectories
cwd_init = {}
count = 0
while cwd_init != cwd:
    count += 1
    cwd_init = copy.deepcopy(cwd)
    
    for wd, wd_list in cwd.items():
        for sub_dir in wd_list:
            if len(cwd[sub_dir]) > 0:
                for sub_dir2 in cwd[sub_dir]:
                    if not sub_dir2 in cwd[wd]:
                        cwd[wd].append(sub_dir2)
    if count > 100:
        print('E-stop')
        cwd_init = copy.deepcopy(cwd)
       
        
#Sum up the size of all directories    
wd_size = pd.DataFrame(columns = ['dir', 'size'])
temp_size = 0
for wd in cwd.keys():
    temp_size = files[files['dir'] == wd]['size'].sum() 
    for sub_dir in cwd[wd]:
        temp_size += files[files['dir'] == sub_dir]['size'].sum() 

    wd_size.loc[len(wd_size.index)] = [wd, temp_size] 
        
big_sz = wd_size[wd_size['size'] <= 100000]['size'].sum() 

wd_size.sort_values('size', inplace=True)

total_size = wd_size['size'].max()
if total_size > 40000000:
    free_space_needed = total_size - 40000000
else:
    print('Free space not needed')

print(files['size'].sum())
print(free_space_needed)
wd2 = wd_size[wd_size['size'] >= free_space_needed]
wd3 = wd_size[wd_size['size'] < free_space_needed]



print(wd_size.to_string())
#print(wd2) 
#print(wd3)

print('Directory to delete = ', wd2['dir'].iloc[0])
print('Directory size = ', wd2['size'].iloc[0])                
print('Sum of all directories > 100000 = ', big_sz)
print('Number of loops = ', count)
print('Number of directories ', len(wd_size))
