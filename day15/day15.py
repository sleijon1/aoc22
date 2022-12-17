from collections import defaultdict
import re

sensors = open("input.txt").read().splitlines()
points = defaultdict(lambda: ".")

def calc_overlap(square_1, square_2):
    overlap_x = min(square_1[0]) > min(square_2[0]) and max(square_2[0]) > max(square_1[0])\
                or min(square_2[0]) > min(square_1[0]) and max(square_1[0]) > max(square_2[0])
    overlap_y = min(square_1[1]) > min(square_2[1]) and max(square_2[1]) > max(square_1[1])\
                or min(square_2[1]) > min(square_1[1]) and max(square_1[1]) > max(square_2[1])
    if overlap_x and overlap_y:
        left_x, right_x = min(square_1[0], square_2[0]), min(square_1[0], square_2[0])
        left_y, right_y = min(square_1[1], square_2[1]), min(square_1[1], square_2[1])
    return


def reduce_ranges(ranges):
    pass



def manhattan(p1, p2):
    s_x, s_y = p1
    b_x, b_y = p2
    left_x, right_x = min(s_x, b_x), max(s_x, b_x)
    left_y, right_y = min(s_y, b_y), max(s_y, b_y)
    mh_dist = abs(left_x - right_x) + abs(left_y - right_y)
    return mh_dist

rows = defaultdict(list)
for sensor in sensors:
    s_x, s_y, b_x, b_y = map(lambda x: int(x.strip("=")), re.findall('=[-]?[0-9]+', sensor))
    #print("SENSOR", (s_x, s_y))
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

print("have we done this mate?")
bounds = 4000000
for y in range(bounds+1):
    ranges = rows[y]
    print(y)
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
            print("BEACON MIGHT BE HERE MATE", beacon_point)
            print(f"Tuning frequency {beacon_point[0]*4000000+y}")
            exit()

        


