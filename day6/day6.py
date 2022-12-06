from aocutils.clients.client import fetch, submit

fetch()

characters = open("day6/inputs.txt").read().strip()
def find_sequence(length):
    value = 0
    for i, _ in enumerate(characters):
        if len(set(characters[i:i+length])) == length:
            value = i+length
            break
    return value

submit(find_sequence(14), level=2)