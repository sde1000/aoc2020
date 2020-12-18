#!/usr/bin/env python3

import operator

# Tokens are all single characters so we can parse without backtracking

def tokenise(i):
    try:
        while True:
            t = next(i)
            if t in "0123456789":
                yield int(t)
            elif t in "+*":
                yield t
            elif t == "(":
                yield list(tokenise(i))
            elif t == ")":
                return
    except StopIteration:
        return

with open("day18-input.txt") as f:
    homework = [ list(tokenise(iter(l))) for l in f ]

def eval_lr(tokens):
    t = list(tokens)
    l = t.pop(0)
    if isinstance(l, list):
        l = eval_lr(l)
    while len(t) > 0:
        op = t.pop(0)
        r = t.pop(0)
        if isinstance(r, list):
            r = eval_lr(r)
        if op == '+':
            l = l + r
        else:
            l = l * r
    return l

print(f"Part one: {sum(eval_lr(h) for h in homework)}")

def eval_add(tokens):
    t = list(tokens)
    def eval_op(c, op):
        nonlocal t
        while c in t:
            i = t.index(c)
            r = t.pop(i + 1)
            l = t.pop(i - 1)
            if isinstance(l, list):
                l = eval_add(l)
            if isinstance(r, list):
                r = eval_add(r)
            t[i - 1] = op(l, r)
    eval_op('+', operator.add)
    eval_op('*', operator.mul)
    return t[0]

print(f"Part two: {sum(eval_add(h) for h in homework)}")
