#!/usr/bin/env python3

def passports():
    with open('input.txt') as f:
        r = {}
        for l in f.readlines():
            pairs = l.split()
            if not pairs:
                yield r
                r = {}
            for pair in pairs:
                key, val = pair.split(':', 1)
                r[key] = val
        if r:
            yield r

def valid(p):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for r in req:
        if r not in p:
            return False
    return True

count = 0
for p in passports():
    if valid(p):
        count += 1

print(count)
