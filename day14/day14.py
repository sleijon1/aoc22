from collections import defaultdict

def generate_spots():
    lines = open("input.txt").read().splitlines()

    spots = defaultdict(lambda: ".")
    ranges = []
    for line in lines:
        new_range = []
        for coords in line.split(" -> "):
            x, y = map(int, coords.split(','))
            new_range.append((x, y))
        ranges.append(new_range)

    max_depth, max_width = 0, 0
    for new_range in ranges:
        i = 0
        while i < len(new_range)-1:
            r1, r2 = new_range[i], new_range[i+1]
            x_range = range(min(r1[0], r2[0]), max(r1[0], r2[0])+1) 
            y_range = range(min(r1[1], r2[1]), max(r1[1], r2[1])+1)
            x_range = x_range if x_range else [r1[0]]
            y_range = y_range if y_range else [r1[1]]
            for x in x_range:
                for y in y_range:
                    spots[(x, y)] = "#"
                    if y > max_depth:
                        max_depth = y
                    if x > max_width:
                        max_width = x
            i += 1
    return spots, max_depth

def count_sand(spots, max_depth, b=False):
    while True:
        old_spot = (500, 0)
        while True:
            possible_moves = [(0, 1), (-1, 1), (1, 1)]
            descending = False
            for move in possible_moves:
                new_spot = (old_spot[0] + move[0], old_spot[1] + move[1])
                if spots[new_spot] not in ('o', '#'):
                    old_spot = new_spot
                    if b and (new_spot[1] == max_depth-1):
                        break
                    descending = True
                    if new_spot[1] == max_depth and not b:
                        return len([val for val in spots.values() if val =='o'])
                    break
            if descending:
                continue
            else:
                spots[old_spot] = 'o'
                if old_spot == (500, 0) and b:
                    return len([val for val in spots.values() if val =='o'])
                break

spots, depth = generate_spots()
print(count_sand(spots, depth))
spots_b, depth_b = generate_spots()
print(count_sand(spots, depth+2, b=True))
            