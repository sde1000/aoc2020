#!/usr/bin/env python3

import re

pre = re.compile(r'^(\d+)-(\d+) (.): (.*)$')

valid = 0
with open('input.txt') as f:
    for l in f.readlines():
        m = pre.match(l)
        lowest = int(m.group(1))
        highest = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        if password[lowest - 1] == letter and password[highest - 1] != letter \
           or password[lowest - 1] != letter and password[highest - 1] == letter:
            valid += 1

print(valid)

