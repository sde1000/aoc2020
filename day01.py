#!/usr/bin/env python3

import itertools

with open('day01-input.txt') as f:
    er = [ int(x) for x in f ]

for x, y in itertools.combinations(er, 2):
    if x + y  == 2020:
        print(f"Part one: {x * y}")
        break

for x, y, z in itertools.combinations(er, 3):
    if x + y + z == 2020:
        print(f"Part two: {x * y * z}")
        break
