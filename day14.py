#!/usr/bin/env python3

import re

mem_re = re.compile(r'^mem\[(\d+)\] = (\d+)$')

def parse(f):
    for l in f:
        if l.startswith("mask = "):
            mask = l.strip()[7:]
        else:
            m = mem_re.match(l)
            yield mask, int(m.group(1)), int(m.group(2))

with open("day14-input.txt") as f:
    prog = list(parse(f))

mem = {}
for mask, addr, val in prog:
    mem[addr] = val \
        & int(mask.replace('X', '1'), 2) \
        | int(mask.replace('X', '0'), 2)

print(f"Part one: {sum(mem.values())}")

def bits(i):
    while True:
        yield '1' if i & 1 else '0'
        i = i >> 1

def mask_addr(mask, addr):
    return ''.join(reversed(list(
        l if m == '0' else m
        for m, l in zip(reversed(mask), bits(addr)))))

def all_addrs(mask):
    mask = list(reversed(mask))
    for i in range(pow(2, mask.count('X'))):
        v = bits(i)
        a = [ next(v) if m == 'X' else m for m in mask ]
        yield int(''.join(reversed(a)), 2)

mem = {}
for mask, addr, val in prog:
    for loc in all_addrs(mask_addr(mask, addr)):
        mem[loc] = val

print(f"Part two: {sum(mem.values())}")
