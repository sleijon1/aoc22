from collections import defaultdict
import re
from time import time

start = time()
sensors = open("input.txt").read().splitlines()
points = defaultdict(lambda: ".")


def manhattan(p1, p2):
    s_x, s_y = p1
    b_x, b_y = p2
    left_x, right_x = min(s_x, b_x), max(s_x, b_x)
    left_y, right_y = min(s_y, b_y), max(s_y, b_y)
    mh_dist = abs(left_x - right_x) + abs(left_y - right_y)
    return mh_dist

row = 2000000
rows = defaultdict(list)
for sensor in sensors:
    s_x, s_y, b_x, b_y = map(lambda x: int(x.strip("=")), re.findall('=[-]?[0-9]+', sensor))
    points[(s_x, s_y)] = "S"
    points[(b_x, b_y)] = "B"
    mh_dist = manhattan((s_x, s_y), (b_x, b_y))
    y_top = s_y+mh_dist+1
    y_bot = s_y-mh_dist
    # this will include perimeter
    for i, j in enumerate(range(y_top, s_y-1, -1)):
        rows[j].append([s_x-i, s_x+i])
    for i, j in enumerate(range(y_bot-1, s_y)):
        rows[j].append([s_x-i, s_x+i])

    if row in range(y_bot, y_top):
        y_range = [row]
        for new_x in range(s_x-mh_dist, s_x+mh_dist+1):
            for new_y in y_range:
                if manhattan((s_x, s_y), (new_x, new_y)) <= mh_dist:
                    points[(new_x, new_y)] = "#"


def find_beacon():
    bounds = 4000000
    for y in range(bounds+1):
        ranges = rows[y]
        beacon_point = None
        for i in range(len(ranges)):
            for perimeter_point in ranges[i]:
                if not (bounds >= perimeter_point >= 0):
                    continue
                possible_beacon = True
                for j in range(len(ranges)):
                    if i != j:
                        if perimeter_point in range(ranges[j][0]+1, ranges[j][1]):
                            possible_beacon = False
                            break
                if possible_beacon:
                    beacon_point = (perimeter_point, y)
                    break
            if possible_beacon:
                return beacon_point[0]*4000000+y


points_on_row = [point for point, value in points.items() 
                 if value not in ("B", ".") and point[1] == row]

print(f"Positions cannot contain beacon: {len(points_on_row)}")
print(f"Tuning frequency {find_beacon()}")
print(f"Took {time()-start} seconds")


