#!/usr/bin/env python3
with open("day08-input.txt") as f:
    instructions = [ (x.split()[0], int(x.split()[1])) for x in f ]

def run(program):
    pc = 0
    acc = 0
    while True:
        yield pc, acc
        op, arg = program[pc]
        if op == "acc":
            acc += arg
            pc += 1
        elif op == "jmp":
            pc += arg
        else:
            pc += 1
        if pc == len(program):
            return

def check(program):
    visited = set()
    for loc, acc in run(program):
        if loc in visited:
            return acc, False
            break
        visited.add(loc)
    return acc, True

print(f"Part one: {check(instructions)[0]}")

def vary(program):
    for loc, code in enumerate(program):
        op, arg = code
        if op in ("nop", "jmp"):
            variant = list(program)
            variant[loc] = ("jmp" if op == "nop" else "nop", arg)
            yield variant

for variant in vary(instructions):
    acc, terminated = check(variant)
    if terminated:
        print(f"Part two: {acc}")
        break
