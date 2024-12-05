"""
Advent of Code 2024
Day 3
"""
import numpy as np

def check_report(report):
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
    return status


with open('d2_input.txt') as f:
    lines = f.readlines()

safe, unsafe, semisafe = 0, 0, 0
for line in lines:
    report = [int(x.strip()) for x in line.split()]
    status = check_report(report)
    if status:
        safe += 1
    else:
        unsafe += 1
        for i in range(len(report)):
            report2 = report[:i] + report[i+1:]
            status = check_report(report2)
            if status:
                semisafe += 1
                unsafe -= 1
                break


print('Total reports:', len(lines), 'Safe:', safe, 'Semisafe:', semisafe, 'Unsafe:', unsafe)
print('Total safe:', safe + semisafe)