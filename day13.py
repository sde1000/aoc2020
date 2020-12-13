#!/usr/bin/env python3

# NB requires python 3.8 for modular inverse

with open("day13-input.txt") as f:
    earliest = int(f.readline())
    schedule = [ None if x == 'x' else int(x) for x in f.readline().split(',') ]

def wait_time(bus):
    missed_by = earliest % bus
    return bus - missed_by if missed_by else 0

waits = { wait_time(bus): bus for bus in schedule if bus }

print(f"Part one: {waits[min(waits.keys())] * min(waits.keys())}")

# Part two: Turn the bus schedule into a list of congruences, then
# solve using the Chinese Remainder Theorem
#
# Eg. the example turns into:
#  t ≡ (7 - 0) (mod 7)
#  t ≡ (13 - 1) (mod 13)
#  t ≡ (59 - 4) (mod 59)
#  t ≡ (31 - 6) (mod 31)
#  t ≡ (19 - 7) (mod 19)

c = [ (bus, bus - offset)
      for offset, bus in enumerate(schedule) if bus ]

from functools import reduce

def chinese_remainder(c):
    s = 0
    prod = reduce(lambda a, b: a * b, (x[0] for x in c))
    for n, a in c:
        p = prod // n
        s += a * pow(p, -1, n) * p
    return s % prod

print(f"Part two: {chinese_remainder(c)}")
