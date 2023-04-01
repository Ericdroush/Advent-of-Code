# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:07:22 2022

@author: ericd
"""

with open('../Input/d2_input.txt') as f:
    lines = f.readlines()

def calc_score(inp1, inp2):
    if inp1 == "A" and inp2 == "X":
        pts = 3 + 1
    elif inp1 == "A" and inp2 == "Y":
        pts = 6 + 2
    elif inp1 == "A" and inp2 == "Z":
        pts= 0 + 3
    elif inp1 == "B" and inp2 == "X":
        pts = 0 + 1
    elif inp1 == "B" and inp2 == "Y":
        pts = 3 + 2
    elif inp1 == "B" and inp2 == "Z":
        pts = 6 + 3
    elif inp1 == "C" and inp2 == "X":
        pts = 6 + 1
    elif inp1 == "C" and inp2 == "Y":
        pts = 0 + 2
    elif inp1 == "C" and inp2 == "Z":
        pts = 3 + 3
    return pts

def calc_score2(inp1, inp2):
    #x = lose, y = draw, z = win
    if inp1 == "A" and inp2 == "X":
        pts = 0 + 3
    elif inp1 == "A" and inp2 == "Y":
        pts = 3 + 1
    elif inp1 == "A" and inp2 == "Z":
        pts = 6 + 2
    elif inp1 == "B" and inp2 == "X":
        pts = 0 + 1
    elif inp1 == "B" and inp2 == "Y":
        pts = 3 + 2
    elif inp1 == "B" and inp2 == "Z":
        pts = 6 + 3
    elif inp1 == "C" and inp2 == "X":
        pts = 0 + 2
    elif inp1 == "C" and inp2 == "Y":
        pts = 3 + 3
    elif inp1 == "C" and inp2 == "Z":
        pts = 6 + 1
    return pts

round_count = 0
score = 0
score2 = 0
for line in lines:
    round_count += 1
    score = score + calc_score(line[0], line[2])
    score2 = score2 + calc_score2(line[0], line[2])
    
print('Total rounds played = ', round_count)
print('Total Score1 = ', score)
print('Total Score2 = ', score2)