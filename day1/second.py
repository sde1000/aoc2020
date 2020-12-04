#!/usr/bin/env python3

with open('input.txt') as f:
    er = [ int(x) for x in f.readlines() ]

for x, y, z in ( (x, y, z) for x in er for y in er for z in er):
    if x + y + z == 2020:
        print(x * y * z)
        break
