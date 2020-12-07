#!/usr/bin/env python3

import functools

with open("day6-input.txt") as f:
    groups = [ [ { a for a in answer} for answer in g.split("\n") ] for g in f.read().strip().split("\n\n") ]

g1 = [ len(functools.reduce(lambda a,b:a|b, g)) for g in groups ]
print(f"Part one: {sum(g1)}")

g2 = [ len(functools.reduce(lambda a,b:a&b, g)) for g in groups ]
print(f"Part two: {sum(g2)}")
