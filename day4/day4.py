from aocutils.clients.client import fetch, submit
import re

fetch()

pairs = open("day4/input.txt").read().splitlines()

full_overlap, overlap = 0, 0
for pair in pairs:
    ints = re.findall('[0-9]+', pair)
    s1_range = range(int(ints[0]), int(ints[1])+1)
    s2_range = range(int(ints[2]), int(ints[3])+1)
    intersect = set(s1_range).intersection(s2_range)
    if len(intersect) == len(s1_range) or len(intersect) == len(s2_range):
        full_overlap += 1
    if intersect:
        overlap += 1

print(full_overlap, overlap)
