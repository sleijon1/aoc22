from aocutils.clients.client import fetch, submit

fetch()

characters = open("day6/input.txt").read().strip()
def find_sequence(length):
    for i, _ in enumerate(characters):
        if len(set(characters[i:i+length])) == length:
            return i+length

print(find_sequence(4), find_sequence(14))
# submit(find_sequence(4), level=1)
# submit(find_sequence(14), level=2)