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
        count = password.count(letter)
        if count >= lowest and count <= highest:
            valid += 1

print(valid)

