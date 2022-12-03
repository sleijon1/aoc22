from aocutils.clients.client import submit, fetch

fetch()

rucksacks = open("day3/input.txt").read().splitlines()

priorities_1, priorities_2 = 0, 0
last_three = []

def calc_prio(in_common):
    priorities = 0
    for char in in_common:
        if char.isupper():
            priorities += ord(char) - 38
            continue
        priorities += ord(char) - 96
    return priorities

for rucksack in rucksacks:
    half = len(rucksack)//2
    in_common = set(rucksack[:half]).intersection(set(rucksack[half:]))
    priorities_1 += calc_prio(in_common)
    last_three.append(rucksack)
    if len(last_three) == 3:
        in_common_2 = set(last_three[0]).intersection(set(last_three[1]), set(last_three[2]))
        priorities_2 += calc_prio(in_common_2)
        last_three = []

print(priorities_1)
print(priorities_2)
# submit(priorities_1)
# submit(priorities_2)