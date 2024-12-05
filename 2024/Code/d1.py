"""
Advent of Code 2024
Day 1
"""

with open('d1_input.txt') as f:
    lines = f.readlines()

a, b = [], []

for line in lines:
    a.append(int(line.split()[0].strip()))
    b.append(int(line.split()[1].strip()))

a.sort()
b.sort()

dist, sim = 0, 0
for i in range(len(a)):
    dist += abs(a[i] - b[i])
    sim += a[i] * b.count(a[i])

print('Distance:', dist, 'Similarity:', sim)