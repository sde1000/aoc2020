#!/usr/bin/env python3

import itertools

cups_input = "614752839"

# To make things easier for ourselves, we're going to use cups
# labelled from 0 to n - 1 and convert at the start and end of the
# problem.

# We store the cup positions as a linked list.
# element n is the label of the cup after n
# head is the label of the current cup

def init(data):
    data = [ x - 1 for x in data ]
    l = [ None ] * len(data)
    h = data[0]
    for d in reversed(data):
        l[d] = h
        h = d
    return h, l

def dump(head, l):
    i = head
    r = []
    while True:
        r.append(i + 1)
        i = l[i]
        if i == head:
            break
    return r

def move(head, l):
    picked = []
    i = head
    for _ in range(3):
        i = l[i]
        picked.append(i)
    destination = (head - 1) % len(l)
    while destination in picked:
        destination = (destination - 1) % len(l)
    l[head] = l[picked[-1]]
    l[picked[-1]] = l[destination]
    l[destination] = picked[0]
    return l[head]

head, l = init(int(x) for x in cups_input)
for _ in range(100):
    head = move(head, l)
print(f"Part one: {''.join(str(x) for x in dump(0, l))[1:]}")

head, l = init(itertools.chain((int(x) for x in cups_input),
                               range(len(cups_input) + 1, 1000001)))
for _ in range(10000000):
    head = move(head, l)

c_1 = l[0]
c_2 = l[c_1]

print(f"Part two: {(c_1 + 1) * (c_2 + 1)}")
