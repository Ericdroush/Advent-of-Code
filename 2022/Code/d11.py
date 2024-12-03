# -*- coding: utf-8 -*-
"""
Created on Sat Apr 1 

@author: ericdroush
"""
import numpy as np

with open('../Input/d11_input.txt') as f:
    inp = f.readlines()

num_rounds = 10000  #Set to 20 for part 1 and 1000 for part 2
worry_val = 1   #Set to 3 for part 1, and 1 for part 2
count = 0

items = []
operation = []
test = []
t_val = []
f_val = []
gcd = 1

for i in range(len(inp)):
    if inp[i][0] == 'M':
        count += 1
        m_id = int(inp[i].split()[1].strip().replace(':',''))
        i += 1
        items.append(inp[i].split(':')[1].strip().split(','))
        i += 1
        operation.append(inp[i].split('=')[1].strip())
        i += 1
        test.append(int(inp[i].strip().split()[-1]))
        gcd *= test[-1]
        i += 1
        t_val.append(int(inp[i].strip().split()[-1]))
        i += 1
        f_val.append(int(inp[i].strip().split()[-1]))


inspect = np.zeros(count)

for round in range(num_rounds):
    for monkey in range(count):
        for item in items[monkey]:
            inspect[monkey] += 1
            t = eval(operation[monkey].replace('old', str(item))) // worry_val
            t %= gcd   #line added for part too
            if t % test[monkey] == 0:
                items[t_val[monkey]].append(t)
            else:
                items[f_val[monkey]].append(t)
        items[monkey] = []   #Clear out the list, all items have been passe to other monkeys
    if round % 100 == 0:
        print('After ', round, ',', items)  
        
    
    
    
print(inspect)  
inspect2 = np.sort(inspect)
print(inspect2)
mb = inspect2[-1] * inspect2[-2] 
print('The monkey business is', int(mb)) 
    
    
    