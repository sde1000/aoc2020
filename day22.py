#!/usr/bin/env python3

with open("day22-input.txt") as f:
    h1, h2 = f.read().split("\n\n")
    h1 = [ int(x) for x in h1.splitlines()[1:] ]
    h2 = [ int(x) for x in h2.splitlines()[1:] ]

def score(c):
    return sum(i * c for i, c in enumerate(reversed(c), start=1))

def game(h1, h2, recursive=False):
    h1 = list(h1)
    h2 = list(h2)
    seen = set()
    while len(h1) > 0 and len(h2) > 0:
        game_state = (tuple(h1), tuple(h2))
        if recursive and game_state in seen:
            return 1, 0
        seen.add(game_state)
        c1 = h1.pop(0)
        c2 = h2.pop(0)
        if recursive and len(h1) >= c1 and len(h2) >= c2:
            s1, s2 = game(h1[:c1], h2[:c2], recursive=True)
        else:
            s1, s2 = c1, c2
        if s1 > s2:
            h1.append(c1)
            h1.append(c2)
        else:
            h2.append(c2)
            h2.append(c1)
    return score(h1), score(h2)

print(f"Part one: {max(game(h1, h2))}")
print(f"Part two: {max(game(h1, h2, recursive=True))}")
