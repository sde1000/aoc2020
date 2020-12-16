#!/usr/bin/env python3

import itertools
import functools
import operator

with open("day16-input.txt") as f:
    rules, my_ticket, nearby_tickets = f.read().split("\n\n")

def parse_rule(r):
    name, ranges = r.split(":")
    ranges = ranges.split(" or ")
    a, b = ranges[0].split("-")
    c, d = ranges[1].split("-")
    return name, int(a), int(b), int(c), int(d)

rules = { n: (a, b, c, d) for n, a, b, c, d in (
    parse_rule(x) for x in rules.splitlines()) }

my_ticket = [ int(x) for x in my_ticket.splitlines()[-1].split(',') ]

nearby_tickets = [ [ int(x) for x in l.split(',') ]
                   for l in nearby_tickets.splitlines()[1:] ]

def valid(rule, num):
    a, b, c, d = rule
    return (num >= a and num <= b) or (num >= c and num <= d)

def valid_for_any(num):
    for rule in rules.values():
        if valid(rule, num):
            return True
    return False

values = itertools.chain.from_iterable(nearby_tickets)
print(f"Part one: {sum(v for v in values if not valid_for_any(v))}")

valid_tickets = [
    x for x in nearby_tickets
    if sum(not valid_for_any(i) for i in x) == 0 ]

possible_fields = [ set(rules.keys()) for i in range(len(my_ticket)) ]
for t in valid_tickets:
    for poss, v in zip(possible_fields, t):
        for field, rule in rules.items():
            if not valid(rule, v):
                poss.discard(field)

while len([f for f in possible_fields if len(f) != 1]):
    unambiguous = [ f for f in possible_fields if len(f) == 1 ]
    for p in possible_fields:
        for u in unambiguous:
            if p is not u:
                p.difference_update(u)
fields = [ list(f)[0] for f in possible_fields ]

departures = functools.reduce(
    operator.mul, ( x for x, f in zip(my_ticket, fields)
                    if f.startswith("departure") ))
print(f"Part two: {departures}")
