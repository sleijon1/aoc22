from aocutils.clients.client import fetch, submit

fetch()

lines = open("day9/input.txt").read().splitlines()


def adjacent(x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    adjacent = []
    for i, j in directions:
        new_x = x + i
        new_y = y + j
        adjacent.append((new_x, new_y))
    return adjacent


rope = [(0, 0) for _ in range(10)]
visited = [[] for _ in range(9)]
directions = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}
for line in lines:
    dir_, count = line.split(" ")
    for _ in range(int(count)):
        i = 9
        while i >= 1:
            visited[i-1].append((rope[i-1][0], rope[i-1][1]))
            if i == 9:
                head_x_move, head_y_move = directions[dir_]
                rope[i] = (rope[i][0]+head_x_move, rope[i][1]+head_y_move)

            if ((rope[i][0], rope[i][1]) in adjacent(rope[i-1][0], rope[i-1][1])) or\
               (rope[i][0], rope[i][1]) == (rope[i-1][0], rope[i-1][1]):
                break
            else:
                for adj_x, adj_y in adjacent(rope[i][0], rope[i][1]):
                    if (adj_x, adj_y) in adjacent(rope[i-1][0], rope[i-1][1]):
                        rope[i-1] = (adj_x, adj_y)
                        visited[i-1].append((rope[i-1][0], rope[i-1][1]))
                        i -= 1
                        break

print(len(set(visited[0])), len(set(visited[-1])))
