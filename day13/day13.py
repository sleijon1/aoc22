from aocutils.clients.client import fetch, submit
from itertools import zip_longest

fetch()

pairs = open("day13/input.txt").read().split('\n\n')


def parse_packet(packet, curr_list=None, i=0, depth_list=[]):
    if packet[i] == "[":
        new_list = []
        if curr_list is not None:
            curr_list.append(new_list)
            depth_list.append(curr_list)
        curr_list = new_list
        i += 1
    elif packet[i] == "]":
        if i == len(packet)-1:
            return curr_list
        curr_list = depth_list.pop()
        i += 1
    else:
        start = i
        while packet[i] not in ('[', ']'):
            i += 1
        if ',' not in packet[start:i]:
            ints = ("".join(packet[start:i])+",").split(',')
        else:
            ints = ("".join(packet[start:i])).split(',')
        for integer in ints:
            if not integer:
                continue
            curr_list.append(int(integer))
    return parse_packet(packet, curr_list, i, depth_list)


def packets_in_order(p1, p2):
    in_order = None
    for item1, item2 in zip_longest(p1, p2):
        if item2 is None and item1 is not None:
            in_order = False
        elif item1 is None and item2 is not None:
            in_order = True
        elif type(item1) == list and type(item2) != list:
            in_order = packets_in_order(item1, [item2])
        elif type(item1) != list and type(item2) == list:
            in_order = packets_in_order([item1], item2)
        elif type(item1) == list and type(item2) == list:
            in_order = packets_in_order(item1, item2)
        elif type(item1) == int and type(item2) == int:
            if item1 < item2:
                in_order = True
            if item1 > item2:
                in_order = False
        if in_order is not None:
            return in_order


def sum_in_order(pairs):
    sum_indices = 0
    for i, pair in enumerate(pairs):
        p1, p2 = map(list, pair.split('\n'))
        p1, p2 = parse_packet(p1), parse_packet(p2)
        in_order = packets_in_order(p1, p2)
        if in_order:
            sum_indices += i+1
    return sum_indices

print(sum_in_order(pairs))

pairs = (open("day13/input.txt").read() + "\n\n[[2]]\n[[6]]").split('\n\n')
packets = []
for i, pair in enumerate(pairs):
    p1, p2 = map(list, pair.split('\n'))
    p1, p2 = parse_packet(p1), parse_packet(p2)
    packets.append(p1)
    packets.append(p2)

ordered = 0
while ordered < len(packets)-1:
    ordered = 0
    i = 0
    while i < len(packets)-1:
        if not packets_in_order(packets[i], packets[i+1]):
            first_packet = packets[i]
            packets[i] = packets[i+1]
            packets[i+1] = first_packet
        else:
            ordered += 1
        i += 1

decoder_key = (packets.index([[6]])+1) * (packets.index([[2]])+1)
print(decoder_key)
#submit(answer=decoder_key, level=2)
