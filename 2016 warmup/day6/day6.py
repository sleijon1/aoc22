from aocutils.clients.client import fetch, submit
from collections import Counter

sequences = open("2016 warmup/day6/input.txt").read().splitlines()
code_a, code_b = [], []
columns = [[] for _ in range(len(sequences[0]))]
for sequence in sequences:
    for i, character in enumerate(sequence):
        columns[i].append(character)

for column in columns:
    counter = Counter()
    counter.update(column)
    code_a.append(counter.most_common(1)[0][0])
    code_b.append(counter.most_common()[-1][0][0])

print("".join(code_a), "".join(code_b))