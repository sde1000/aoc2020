#!/usr/bin/env python3

import re
rule_re = re.compile("^(.+) bags contain (.+)\.$")
bag_re = re.compile("^(\d+) (.+) bags?$")

def bag_contents(x):
    if x == "no other bags":
        return []
    return [ (int(m.group(1)), m.group(2)) for m in (
        bag_re.match(b) for b in x.split(', ') ) ]

with open("day7-input.txt") as f:
    rules = { m.group(1): bag_contents(m.group(2)) for m in (
        rule_re.match(l) for l in f ) }

def expand(bag):
    for number, colour in rules[bag]:
        yield colour
        yield from expand(colour)

print(f"Part one: {sum(1 if 'shiny gold' in expand(b) else 0 for b in rules.keys())}")

def expand_fully(bag):
    for number, colour in rules[bag]:
        for x in range(number):
            yield colour
            yield from expand_fully(colour)

print(f"Part two: {len(list(expand_fully('shiny gold')))}")
