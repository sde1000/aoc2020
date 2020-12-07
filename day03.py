#!/usr/bin/env python3

with open('day03-input.txt') as f:
    trees = [ x.strip() for x in f ]

def check(right, down):
    x = 0
    count = 0
    for l in trees[::down]:
        if x >= len(l):
            x -= len(l)
        if l[x] == '#':
            count += 1
        x += right
    return count

print(f"Part one: {check(3, 1)}")

r = 1
for i in [check(1, 1),
          check(3, 1),
          check(5, 1),
          check(7, 1),
          check(1, 2)]:
    r = r * i

print(f"Part two: {r}")
