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
    indexed_row = re.findall(r"([A-Z]|    )", line)
    for i, value in enumerate(indexed_row):
        if value[0] != " ":
            stacks[i+1].insert(0, value)

stacks_b = deepcopy(stacks)
for instruction in instructions.splitlines():
    move, from_, to = map(int, re.findall('[0-9]+', instruction))
    stacks[to] += stacks[from_][-move:][::-1]
    stacks[from_] = stacks[from_][:-move]
    stacks_b[to] += stacks_b[from_][-move:]
    stacks_b[from_] = stacks_b[from_][:-move]


answer = "".join([val[-1].strip("[").strip("]") for _, val in sorted(stacks.items(), key=lambda x: x[0])])
answer_b = "".join([val[-1].strip("[").strip("]") for _, val in sorted(stacks_b.items(), key=lambda x: x[0])])
print(answer, answer_b)
# submit(answer_b, level=2)
