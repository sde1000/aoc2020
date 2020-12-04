#!/usr/bin/env python3

x = 0
count = 0
with open('input.txt') as f:
    for l in f.readlines():
        l = l.strip()
        if x >= len(l):
            x -= len(l)
        if l[x] == '#':
            count += 1
        x += 3

print(count)
