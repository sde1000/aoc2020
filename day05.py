#!/usr/bin/env python3

with open('day05-input.txt') as f:
    seats = [ l.strip() for l in f ]

table = str.maketrans("FBLR", "0101")
seatids = [ int(s.translate(table), 2) for s in seats ]

print(f"Part one: {max(seatids)}")

seatids.sort()
potential_ids = range(min(seatids), max(seatids) + 1)
for mine, possible in zip(potential_ids, seatids):
    if mine != possible:
        print(f"Part two: {mine}")
        break
