#!/usr/bin/env python3

with open("day10-input.txt") as f:
    adapters = [ int(x) for x in f ]

adapters.sort()

ones = 0
threes = 1
for a, b in zip([0] + adapters, adapters):
    if b - a == 1:
        ones += 1
    elif b - a == 3:
        threes += 1

print(f"Part one: {ones * threes}")
    
joltages = { 0: 1 }
def ways_to_reach(j):
    if j < 0:
        return 0
    if j in joltages:
        return joltages[j]
    if j in adapters:
        return (ways_to_reach(j - 1) +
                ways_to_reach(j - 2) +
                ways_to_reach(j - 3))
    return 0

for i in adapters:
    joltages[i] = ways_to_reach(i)

print(f"Part two: {joltages[adapters[-1]]}")
