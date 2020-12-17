#!/usr/bin/env python3

with open("day17-input.txt") as f:
    init = [ l.strip() for l in f ]

# A state is a set of coordinates where a cell is active

def init_state(dimensions):
    s = set()
    for y, l in enumerate(init):
        for x, c in enumerate(l):
            if c == '#':
                s.add((x, y) + (0,) * (dimensions - 2))
    return s

def neighbour_coords(coords):
    x, *xs = coords
    if xs:
        for j in (-1, 0, 1):
            yield from ((x + j,) + k for k in neighbour_coords(xs))
    else:
        for j in (-1, 0, 1):
            yield (x + j,)

def neighbour_count(state, coords):
    return sum(n in state for n in neighbour_coords(coords)
               if n != coords)

def next_coords(state):
    s = set()
    for a in state:
        s.update(set(neighbour_coords(a)))
    return s

def next_state(state):
    s = set()
    for c in next_coords(state):
        if c in state:
            if neighbour_count(state, c) in (2, 3):
                s.add(c)
        else:
            if neighbour_count(state, c) == 3:
                s.add(c)
    return s

def run(dimensions):
    s = init_state(dimensions)
    for i in range(6):
        s = next_state(s)
    return len(s)

print(f"Part one: {run(3)}")
print(f"Part two: {run(4)}")
