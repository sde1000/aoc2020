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
for i in adapters:
    joltages[i] = joltages.get(i - 1, 0) + joltages.get(i - 2, 0) \
        + joltages.get(i - 3, 0)

print(f"Part two: {joltages[adapters[-1]]}")
