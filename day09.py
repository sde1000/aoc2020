#!/usr/bin/env python3

import itertools

with open("day09-input.txt") as f:
    numbers = [ int(l) for l in f ]

window = []
def valid(number):
    if len(window) < 25:
        window.append(number)
        return True
    try:
        for x, y in itertools.combinations(window, 2):
            if x + y == number:
                return True
        return False
    finally:
        window.append(number)
        window.pop(0)

for n in numbers:
    if not valid(n):
        print(f"Part one: {n}")
        break

def check(start, target):
    for l in range(len(numbers) - start):
        s = sum(numbers[start : start + l])
        if s == target:
            return l
        if s > target:
            return

for start in range(len(numbers)):
    r = check(start, n)
    if r:
        cr = numbers[start : start + r]
        print(f"Part two: {min(cr) + max(cr)}")
        break
