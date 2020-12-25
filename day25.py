#!/usr/bin/env python3

card_public = 1327981
door_public = 2822615
gen = 7
mod = 20201227

# It's Christmas Day and I'm in a rush, so let's just brute-force this...

def rev(public):
    i = 1
    while True:
        if pow(gen, i, mod) == public:
            return i
        i += 1

door_secret = rev(door_public)

print(f"Part one: {pow(card_public, door_secret, mod)}")
