from aocutils.clients.client import fetch, submit

fetch()

cmds = open("day7/input.txt").read().splitlines()

stack, sizes = [], {}
popped = []
i = 0
# print(cmds)
end = False
while i < len(cmds):
    # print(cmds[i], i)
    if end or "cd .." in cmds[i]:
        dir_name, subdirs = stack.pop()
        popped.append((dir_name, subdirs))
        i += 1
    elif "cd" in cmds[i] and ".." not in cmds[i]:
        _, _, dir_name = cmds[i].split(" ")
        stack.append([dir_name, []])
        i += 1
    elif "ls" in cmds[i]:
        i += 1
        while "$" not in cmds[i]:
            if "dir" in cmds[i]:
                i += 1
                continue
            size, file_name = cmds[i].split(" ")
            for prev_dir in stack:
                prev_dir[1].append((size, file_name))
            i += 1
            if i == len(cmds):
                end = True
                i -= 1
                break

final = popped + stack
total_sum_100 = 0
sizes = []
for dir_name, sub_dirs in final:
    print(dir_name, sub_dirs)
    sub_dir_sum = sum([int(size) for (size, _) in sub_dirs])
    if sub_dir_sum < 100000:
        total_sum_100 += sub_dir_sum
    sizes.append(sub_dir_sum)
total_sum = sum([int(size) for size, dir_name in stack[0][1]])
unused = 70000000 - total_sum
need = 30000000 - unused
candidates = [size for size in sizes if size >= need]
print(total_sum_100, min(candidates))
# submit(total_sum_100)
# submit(min(candidates), level=2)