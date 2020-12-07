#!/usr/bin/env python3

import re

pre = re.compile(r'^(\d+)-(\d+) (.): (.*)$')

valid_p1 = 0
valid_p2 = 0
with open('day02-input.txt') as f:
    for l in f:
        m = pre.match(l)
        lowest = int(m.group(1))
        highest = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        count = password.count(letter)
        if count >= lowest and count <= highest:
            valid_p1 += 1
        if password[lowest - 1] == letter and password[highest - 1] != letter \
           or password[lowest - 1] != letter and password[highest - 1] == letter:
            valid_p2 += 1

print(f"Part one: {valid_p1}")
print(f"Part two: {valid_p2}")
