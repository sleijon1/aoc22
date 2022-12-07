from aocutils.clients.client import fetch, submit

fetch()

cmds = open("day7/input.txt").read().splitlines()[::-1]

stack, popped = [], []
end, i = False, 0
cmd = cmds.pop()

while cmds:
    if "cd .." in cmd:
        dir_name, subdirs = stack.pop()
        popped.append((dir_name, subdirs))
        cmd = cmds.pop()
    elif "cd" in cmd and ".." not in cmd:
        _, _, dir_name = cmd.split(" ")
        stack.append([dir_name, []])
        cmd = cmds.pop()
    elif "ls" in cmd:
        cmd = cmds.pop()
        while "$" not in cmd:
            if "dir" in cmd:
                cmd = cmds.pop()
                continue
            size, file_name = cmd.split(" ")
            for prev_dir in stack:
                prev_dir[1].append((size, file_name))
            if not cmds:
                break
            cmd = cmds.pop()

final = popped + stack
total_sum_100 = 0
sizes = []
for dir_name, sub_dirs in final:
    sub_dir_sum = sum([int(size) for (size, _) in sub_dirs])
    if sub_dir_sum < 100000:
        total_sum_100 += sub_dir_sum
    sizes.append(sub_dir_sum)
total_sum = sum([int(size) for size, dir_name in stack[0][1]])
need = 30000000 - (70000000 - total_sum)
candidates = [size for size in sizes if size >= need]
print(total_sum_100, min(candidates))
# submit(total_sum_100)
# submit(min(candidates), level=2)