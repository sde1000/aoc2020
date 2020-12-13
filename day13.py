#!/usr/bin/env python3

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

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
 
def chinese_remainder(c):
    s = 0
    prod = reduce(lambda a, b: a * b, (x[0] for x in c))
    for n, a in c:
        p = prod // n
        s += a * mul_inv(p, n) * p
    return s % prod

print(f"Part two: {chinese_remainder(c)}")
