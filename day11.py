#!/usr/bin/env python3

with open("day11-input.txt") as f:
    grid = [ l.strip() for l in f ]

def first_seat(grid, x, y, direction, immediate_only):
    while True:
        x, y = x + direction[0], y + direction[1]
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            break
        if grid[y][x] != '.':
            return grid[y][x]
        if immediate_only:
            break
    return '.'

def neighbours(grid, x, y, immediate_only=True):
    return sum(first_seat(grid, x, y, d, immediate_only) == '#'
               for d in ((-1, -1), (0, -1), (1, -1), (1, 0),
                         (1, 1), (0, 1), (-1, 1), (-1, 0)))

def next_state_p1(grid, x, y):
    s = grid[y][x]
    if s == '.':
        return '.'
    n = neighbours(grid, x, y)
    if s == 'L':
        return '#' if n == 0 else 'L'
    else:
        return 'L' if n >= 4 else '#'

def next_state_p2(grid, x, y):
    s = grid[y][x]
    if s == '.':
        return '.'
    n = neighbours(grid, x, y, immediate_only=False)
    if s == 'L':
        return '#' if n == 0 else 'L'
    else:
        return 'L' if n >= 5 else '#'

def next_grid(grid, f):
    return [ ''.join(f(grid, x, y) for x in range(len(grid[0])))
             for y in range(len(grid)) ]

def occupied(grid, f):
    count = 0
    while True:
        new = next_grid(grid, f)
        if new == grid:
            break
        grid = new
    return sum(x.count('#') for x in grid)

print(f"Part one: {occupied(grid, next_state_p1)}")
print(f"Part two: {occupied(grid, next_state_p2)}")
