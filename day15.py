#!/usr/bin/env python3

i = [5, 2, 8, 16, 18, 0, 1]

def mem(start):
    start = list(start)
    turn = 0
    h = {}
    while True:
        if start:
            num = start.pop(0)
        else:
            last_a, last_b = h.get(num, (0, 0))
            num = last_a - last_b
        yield num
        h[num] = (turn, h.get(num, (turn, turn))[0])
        turn += 1

def th(n, s):
    for _ in range(n):
        r = next(s)
    return r

print(f"Part one: {th(2020, mem(i))}")
print(f"Part two: {th(30000000, mem(i))}")
