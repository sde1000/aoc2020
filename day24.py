#!/usr/bin/env python3

with open("day24-input.txt") as f:
    flip = [ l.strip() for l in f ]

def coords(l):
    i = iter(l)
    x, y = 0, 0
    try:
        while True:
            c = next(i)
            if c == "e":
                x += 1
            elif c == "w":
                x -= 1
            elif c == "n":
                y += 1
                if next(i) == "e":
                    x += 1
            elif c == "s":
                y -= 1
                if next(i) == "w":
                    x -= 1
    except StopIteration:
        pass
    return x, y

black = set()
for l in flip:
    tile = coords(l)
    if tile in black:
        black.remove(tile)
    else:
        black.add(tile)

print(f"Part one: {len(black)}")

# Didn't we do this on day 17?

def neighbour_coords(tile):
    x, y = tile
    return [ (x, y),
             (x, y + 1), (x + 1, y + 1), (x + 1, y),
             (x, y - 1), (x - 1, y - 1), (x - 1, y) ]

def neighbour_count(black, coords):
    return sum(n in black for n in neighbour_coords(coords)
               if n != coords)

def next_coords(black):
    s = set()
    for a in black:
        s.update(set(neighbour_coords(a)))
    return s

def next_state(black):
    s = set()
    for c in next_coords(black):
        if c in black:
            if neighbour_count(black, c) in (1, 2):
                s.add(c)
        else:
            if neighbour_count(black, c) == 2:
                s.add(c)
    return s

for _ in range(100):
    black = next_state(black)

print(f"Part two: {len(black)}")
