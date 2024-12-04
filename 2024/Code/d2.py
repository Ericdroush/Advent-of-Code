"""
Advent of Code 2024
Day 3
"""
import numpy as np

with open('d2_input.txt') as f:
    lines = f.readlines()

safe, unsafe = 0, 0
for line in lines:
    report = [int(x.strip()) for x in line.split()]
    slope = np.sign(report[1] - report[0])
    status = True
    for i in range(len(report) - 1):
        if np.sign(report[i + 1] - report[i]) != slope:
            status = False
            break
        else:
            if abs(report[i + 1] - report[i]) > 3:
                status = False
                break

    if status:
        safe += 1
    else:
        unsafe += 1

print('Total reports:', len(lines), 'Safe:', safe, 'Unsafe:', unsafe)