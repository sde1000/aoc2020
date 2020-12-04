#!/usr/bin/env python3

with open('input.txt') as f:
    er = [ int(x) for x in f.readlines() ]

for x, y in ( (x, y) for x in er for y in er ):
    if x + y == 2020:
        print(x * y)
        break
