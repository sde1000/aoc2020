#!/usr/bin/env python3

from functools import reduce
import operator

def parse_food(l):
    l = l.strip()[:-1]
    ingredients, allergens = l.split(" (contains ")
    return ingredients.split(), allergens.split(", ")

with open("day21-input.txt") as f:
    foods = [ parse_food(l) for l in f ]

allergens = {}
for i, a in foods:
    for allergen in a:
        allergens.setdefault(allergen, set(i)).intersection_update(set(i))

print(f"Part one: {sum(i not in reduce(operator.or_, allergens.values()) for f, a in foods for i in f)}")

while max(len(i) for i in allergens.values()) > 1:
    for i in allergens.values():
        if len(i) == 1:
            for o in allergens.values():
                if o is not i:
                    o.difference_update(i)

dangerous = [ next(iter(allergens[a])) for a in sorted(allergens.keys()) ]

print(f"Part two: {','.join(dangerous)}")
