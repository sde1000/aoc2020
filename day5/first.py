#!/usr/bin/env python3

with open('input.txt') as f:
    seats = [ l.strip() for l in f.readlines() ]

table = str.maketrans("FBLR", "0101")
seatids = [ int(s.translate(table), 2) for s in seats ]

print(max(seatids))
