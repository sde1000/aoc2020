#!/usr/bin/env python3

from functools import reduce
from operator import mul
import math

edges = {}

def rotate(t):
    return list(''.join(l) for l in zip(*reversed(t)))

def flip(t):
    return [ ''.join(reversed(l)) for l in t ]

class tile:
    def __init__(self, d):
        l = d.splitlines()
        self.id = int(l[0][5 : -1])
        self.lines = l[1:]
        for e in range(4):
            edges.setdefault(self.edge_c(e), set()).add(self)
            edges.setdefault(self.edge_a(e), set()).add(self)

    # Edge numbers are: 0=top, 1=right, 2=bottom, 3=left

    # Clockwise
    def edge_c(self, num):
        if num == 0:
            return self.lines[0]
        elif num == 1:
            return ''.join(x[-1] for x in self.lines)
        elif num == 2:
            return ''.join(reversed(self.lines[-1]))
        return ''.join(x[0] for x in reversed(self.lines))        

    # Anticlockwise
    def edge_a(self, num):
        if num == 0:
            return ''.join(reversed(self.lines[0]))
        elif num == 1:
            return ''.join(x[-1] for x in reversed(self.lines))
        elif num == 2:
            return self.lines[-1]
        return ''.join(x[0] for x in self.lines)

    # Rotate clockwise
    def rotate(self):
        self.lines = rotate(self.lines)

    # Flip along vertical line
    def flip(self):
        self.lines = flip(self.lines)

with open("day20-input.txt") as f:
    tiles = [ tile(x) for x in f.read().split("\n\n") ]

edgelen = math.isqrt(len(tiles))

corner_tiles = []
edge_tiles = []
inner_tiles = []
for t in tiles:
    matches = sum(len(edges[c]) - 1 for c in (t.edge_c(i) for i in range(4)))
    if matches == 2:
        corner_tiles.append(t)
    elif matches == 3:
        edge_tiles.append(t)
    else:
        inner_tiles.append(t)

print(f"Part one: {reduce(mul, (x.id for x in corner_tiles))}")

img = [ [ None ] * edgelen for i in range(edgelen) ]

def null_edges(x, y):
    nulls = []
    if x == 0:
        nulls.append(3) # left
    if x == edgelen - 1:
        nulls.append(1) # right
    if y == 0:
        nulls.append(0) # top
    if y == edgelen - 1:
        nulls.append(2) # bottom
    return nulls

def known_edges(x, y):
    knowns = []
    if x > 0:
        # Left edge must match the right edge of the tile to the left
        knowns.append((3, 1, img[y][x - 1]))
    if y > 0:
        # Top edge must match the bottom edge of the tile above
        knowns.append((0, 2, img[y - 1][x]))
    # We are assembling accross from top-left, so we never need to check
    # right or down
    return knowns

def matches(t, nulls, knowns):
    for edgenum in nulls:
        if len(edges[t.edge_c(edgenum)]) != 1:
            return False
    for our_edge, their_edge, other_tile in knowns:
        if t.edge_c(our_edge) != other_tile.edge_a(their_edge):
            return False
    return True

for y in range(edgelen):
    for x in range(edgelen):
        nulls = null_edges(x, y) # list of edges that must not match
        knowns = known_edges(x, y) # list of edges that must match
        if len(nulls) == 2:
            candidates = corner_tiles
        elif len(nulls) == 1:
            candidates = edge_tiles
        else:
            candidates = inner_tiles
        for t in candidates:
            if matches(t, nulls, knowns):
                break
            t.rotate()
            if matches(t, nulls, knowns):
                break
            t.rotate()
            if matches(t, nulls, knowns):
                break
            t.rotate()
            if matches(t, nulls, knowns):
                break
            t.flip()
            if matches(t, nulls, knowns):
                break
            t.rotate()
            if matches(t, nulls, knowns):
                break
            t.rotate()
            if matches(t, nulls, knowns):
                break
            t.rotate()
            if matches(t, nulls, knowns):
                break
        else:
            raise Exception(f"No match found at {x}, {y}")
        candidates.pop(candidates.index(t))
        img[y][x] = t

# Assemble final image
f = []
for row in img:
    for y in range(8):
        f.append(''.join(t.lines[y + 1][1 : -1] for t in row))

def hashes(img):
    return sum(l.count("#") for l in img)

img_hashes = hashes(f)

seamonster = ("                  # ",
              "#    ##    ##    ###",
              " #  #  #  #  #  #   ")

seamonster_hashes = hashes(seamonster)

def check_seamonster(img, x, y):
    for sl, il in zip(seamonster, img[y:]):
        for a, b in zip(sl, il[x:]):
            if a == "#" and b != "#":
                return False
    return True

def count_seamonsters(img):
    count = 0
    for y in range(len(img) - len(seamonster)):
        for x in range(len(img[0]) - len(seamonster[0])):
            if check_seamonster(img, x, y):
                count += 1
    return count

def squint(img):
    # Rotate and flip the image until we see seamonsters
    for r in range(3):
        c = count_seamonsters(img)
        if c:
            return c
        img = rotate(img)
    img = flip(img)
    c = count_seamonsters(img)
    if c:
        return c
    for r in range(3):
        c = count_seamonsters(img)
        if c:
            return c
        img = rotate(img)
    return 0

print(f"Part two: {img_hashes - seamonster_hashes * squint(f)}")
