#!/usr/bin/env python3

import itertools
import functools

def parse_rule(l):
    k, v = l.split(": ")
    if v.startswith('"'):
        return k, v[1]
    return k, [ x.split() for x in v.split(" | ") ]

with open("day19-input.txt") as f:
    rules, messages = f.read().split("\n\n")
    rules = dict(parse_rule(l) for l in rules.splitlines())
    messages = messages.splitlines()

@functools.lru_cache
def expand(rule):
    r = rules[rule]
    if isinstance(r, str):
        return [r]
    return [ ''.join(j) for i in r
             for j in itertools.product(*(expand(x) for x in i)) ]

print(f"Part one: {sum(m in expand('0') for m in messages)}")

rules["8"] = [ ["42"], ["42", "8"] ]
rules["11"] = [ ["42", "31"], ["42", "11", "31"] ]

def part(s, n):
    if n == 1:
        yield (s,)
        return
    for i in range(1, len(s)):
        yield from ((s[:i],) + x for x in part(s[i:], n - 1))

@functools.lru_cache(maxsize=10000000)
def match(s, rule):
    r = rules[rule]
    if isinstance(r, str):
        return r == s
    for alt in r:
        for p in part(s, len(alt)):
            for seg, rule in zip(p, alt):
                if not match(seg, rule):
                    break
            else:
                return True
    return False

print(f"Part two: {sum(match(m, '0') for m in messages)}")
