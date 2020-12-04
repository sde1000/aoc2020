#!/usr/bin/env python3

import re

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

year_re = re.compile(r'^(\d\d\d\d)$')
hgt_re = re.compile(r'^(\d+)(cm|in)$')
hcl_re = re.compile(r'^\#[0-9a-f]{6}$')
ecl_re = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
pid_re = re.compile(r'^\d{9}$')

class Invalid(Exception):
    pass

def check(p, key, re):
    if key not in p:
        raise Invalid()
    r = re.match(p[key])
    if not r:
        raise Invalid()
    return r

def valid(p):
    try:
        byr = int(check(p, 'byr', year_re).group(1))
        if byr < 1920 or byr > 2002:
            return False
        iyr = int(check(p, 'iyr', year_re).group(1))
        if iyr < 2010 or iyr > 2020:
            return False
        eyr = int(check(p, 'eyr', year_re).group(1))
        if eyr < 2020 or eyr > 2030:
            return False
        hgt = check(p, 'hgt', hgt_re)
        hgtval = int(hgt.group(1))
        if hgt.group(2) == "cm":
            if hgtval < 150 or hgtval > 193:
                return False
        else:
            if hgtval < 59 or hgtval > 76:
                return False
        check(p, 'hcl', hcl_re)
        check(p, 'ecl', ecl_re)
        check(p, 'pid', pid_re)
    except Invalid:
        return False
    return True

count = 0
for p in passports():
    if valid(p):
        count += 1

print(count)
