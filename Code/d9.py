# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:30:20 2022

@author: ericd
"""
import numpy as np
import pandas as pd

with open('../Input/d9_input.txt') as f:
    inp = f.readlines()

def mv(hi, ti, hj, tj):
    if hi - ti > 1 and hj == tj:
        ti += 1
    elif ti - hi > 1 and hj == tj:
        ti -= 1
    elif hj - tj > 1 and hi == ti:
        tj += 1
    elif tj - hj > 1 and hi == ti:
        tj -= 1
    if (hi - ti > 1 and hj - tj >= 1) or (hi - ti >= 1 and hj - tj > 1):
        ti += 1
        tj += 1
    if (hi - ti > 1 and tj - hj >= 1) or (hi - ti >= 1 and tj - hj > 1):
        ti += 1
        tj -= 1
    if (ti - hi > 1 and hj - tj >= 1) or (ti - hi >= 1 and hj - tj > 1):
        ti -= 1
        tj += 1
    if (ti - hi > 1 and tj - hj >= 1) or (ti - hi >= 1 and tj - hj > 1):
        ti -= 1
        tj -= 1
    return ti, tj


pos = np.zeros((1000,1000))

number_of_knots = 10
init = 500

loc = []
for i in range(number_of_knots):
    loc.append([init, init])
    
knots = pd.DataFrame(loc, columns = ['y', 'x'])

pos[init, init] = 1
for step in inp:
    step = step.strip()
    direction = step.split()[0]
    count = int(step.split()[1])
    if direction == "D":
        for st in range(count):
            knots.at[0, 'y'] -= 1
            for i in range(1, number_of_knots):
                knots.at[i, 'y'], knots.at[i, 'x'] = mv(knots.at[i - 1, 'y'], knots.at[i, 'y'], knots.at[i - 1, 'x'], knots.at[i, 'x'])            
            pos[knots.at[number_of_knots - 1, 'y'], knots.at[number_of_knots - 1, 'x']] = 1
    if direction == "U":
        for st in range(count):
            knots.at[0, 'y'] += 1
            for i in range(1, number_of_knots):
                knots.at[i, 'y'], knots.at[i, 'x'] = mv(knots.at[i - 1, 'y'], knots.at[i, 'y'], knots.at[i - 1, 'x'], knots.at[i, 'x'])            
            pos[knots.at[number_of_knots - 1, 'y'], knots.at[number_of_knots - 1, 'x']] = 1
    if direction == "L":
        for st in range(count):
            knots.at[0, 'x'] -= 1
            for i in range(1, number_of_knots):
                knots.at[i, 'y'], knots.at[i, 'x'] = mv(knots.at[i - 1, 'y'], knots.at[i, 'y'], knots.at[i - 1, 'x'], knots.at[i, 'x'])            
            pos[knots.at[number_of_knots - 1, 'y'], knots.at[number_of_knots - 1, 'x']] = 1
    if direction == "R":
        for st in range(count):
            knots.at[0, 'x'] += 1
            for i in range(1, number_of_knots):
                knots.at[i, 'y'], knots.at[i, 'x'] = mv(knots.at[i - 1, 'y'], knots.at[i, 'y'], knots.at[i - 1, 'x'], knots.at[i, 'x'])            
            pos[knots.at[number_of_knots - 1, 'y'], knots.at[number_of_knots - 1, 'x']] = 1

print('Total number tail spaces = ', pos.sum())
