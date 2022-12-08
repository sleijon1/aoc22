from aocutils.clients.client import fetch, submit
import math
fetch()

grid = open("day8/input.txt").read().splitlines()
grid = [list(map(int, line)) for line in grid]
columns = [[] for _ in range(len(grid[0]))]
for i, row in enumerate(grid):
    for j, column in enumerate(row):
        columns[j].append(column)

visible, scenic_scores = 0, []
for i, row in enumerate(grid):
    for j, column in enumerate(row):
        added = False
        left, right = row[:j], row[j+1:]
        up, down = columns[j][:i], columns[j][i+1:]
        scenic_dists = 1
        for order, line in enumerate([up, down, left, right]):
            scenic_dist = 0
            distance = [row[j] > tree for tree in line]
            if order in [0, 2]:
                distance = distance[::-1]
            for x in distance:
                if x:
                    scenic_dist += 1
                else:
                    if scenic_dist:
                        scenic_dist += 1
                    break
            scenic_dists *= scenic_dist
            if not added and all(distance):
                visible += 1
                added = True
        scenic_scores.append(scenic_dists)

print(visible)
print(max(scenic_scores))
# submit(answer=visible)
# submit(answer=max(scenic_scores), level=2)