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
row = 2000000
for sensor in sensors:
    s_x, s_y, b_x, b_y = map(lambda x: int(x.strip("=")), re.findall('=[-]?[0-9]+', sensor))
    print("SENSOR", (s_x, s_y))
    points[(s_x, s_y)] = "S"
    points[(b_x, b_y)] = "B"
    mh_dist = manhattan((s_x, s_y), (b_x, b_y))
    x_range = range(s_x-mh_dist, s_x+mh_dist+1)
    y_range = range(s_y-mh_dist, s_y+mh_dist+1)
    if row in y_range:
        y_range = [row]
        for new_x in x_range:
            for new_y in y_range:
                if manhattan((s_x, s_y), (new_x, new_y)) <= mh_dist:
                    points[(new_x, new_y)] = "#"


points_on_row = [point for point, value in points.items() 
                 if value not in ("B", ".") and point[1] == row]
cant_be_beacon = len(points_on_row)
print(cant_be_beacon)