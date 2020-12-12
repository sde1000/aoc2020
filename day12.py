#!/usr/bin/env python3

with open("day12-input.txt") as f:
    moves = [ (a[0], int(a[1:])) for a in f ]

def compass(l, a, v):
    if a == 'N':
        return l[0], l[1] + v
    if a == 'S':
        return l[0], l[1] - v
    if a == 'E':
        return l[0] + v, l[1]
    return l[0] - v, l[1]

def move(direct=True):
    loc = (0, 0)
    if direct:
        vec = (1, 0)
    else:
        vec = (10, 1)
    for a, v in moves:
        if a == 'F':
            loc = (loc[0] + vec[0] * v, loc[1] + vec[1] * v)
        elif a == 'R':
            for _ in range(v // 90):
                vec = (vec[1], -vec[0])
        elif a == 'L':
            for _ in range(v // 90):
                vec = (-vec[1], vec[0])
        else:
            if direct:
                loc = compass(loc, a, v)
            else:
                vec = compass(vec, a, v)
        yield loc

*_, loc = move()
print(f"Part one: {abs(loc[0]) + abs(loc[1])}")

*_, loc = move(direct=False)
print(f"Part two: {abs(loc[0]) + abs(loc[1])}")
