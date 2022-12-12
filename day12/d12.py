from aocutils.clients.client import fetch, submit
from copy import deepcopy
from collections import defaultdict
fetch()

start, starts_b, end = [], [], None
grid = [list(line) for line in open("day12/input.txt").read().splitlines()]
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "S":
            start = [(j, i)]
            grid[i][j] = 'a'
        elif col == "E":
            end = (j, i)
            grid[i][j] = 'z'
        if grid[i][j] == 'a':
            starts_b.append([(j, i)])
        grid[i][j] = ord(grid[i][j])


def bfs(start):
    queue = [start]
    bound_x, bound_y = len(grid[0]), len(grid)
    visited = defaultdict(int)
    while queue:
        queue_item = queue.pop()
        curr_x, curr_y = queue_item[-1]
        for move in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            pos_x, pos_y = [curr_x+move[0], curr_y+move[1]]
            if 0 <= pos_x < bound_x and \
            0 <= pos_y < bound_y and \
            grid[pos_y][pos_x] <= (grid[curr_y][curr_x] + 1) and\
            not visited[(pos_x, pos_y)]:
                new_queue_item = list(queue_item)
                new_queue_item.append((pos_x, pos_y))
                visited[(pos_x, pos_y)] = len(queue_item)
                if (pos_x, pos_y) == end:
                    return len(queue_item)
                else:
                    queue = [new_queue_item] + queue

print(bfs(start))
shortest = None
for start in starts_b:
    dist = bfs(start)
    if shortest is None or dist and dist < shortest:
        shortest = dist
submit(answer=shortest, level=2)
