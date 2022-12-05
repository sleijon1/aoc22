from aocutils.clients.client import fetch, submit
import re
from collections import defaultdict
from copy import deepcopy

fetch()

crates, instructions = open("day5/input.txt").read().split("\n\n")
rows = crates.splitlines()
stacks = defaultdict(list)
for line in rows[:-1]:
    row_crates = []
    stack_index, empty = 1, 0
    for char in line.split(" "):
        if empty == 4:
            stack_index += 1
            empty = 0
        if char:
            row_crates.append((stack_index, char))
            stack_index += 1
        else:
            empty += 1
    for i, crate in row_crates:
        stacks[i].insert(0, crate)

stacks_b = deepcopy(stacks)
for instruction in instructions.splitlines():
    move, from_, to = map(int, re.findall('[0-9]+', instruction))
    for _ in range(move):
        stacks[to].append(stacks[from_].pop())
    stacks_b[to] += stacks_b[from_][-move:]
    stacks_b[from_] = stacks_b[from_][:-move]



answer = "".join([val[-1].strip("[").strip("]") for key, val in sorted(stacks.items(), key=lambda x: x[0])])
answer_b = "".join([val[-1].strip("[").strip("]") for key, val in sorted(stacks_b.items(), key=lambda x: x[0])])
# submit(answer_b, level=2)
