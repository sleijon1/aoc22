from aocutils.clients.client import fetch, submit

fetch()

ops = open("day10/input.txt").read().splitlines()

X, last_val, cycle, i = 1, 0, 1, 0
segments = []
crt = [['.' for _ in range(40)] for _ in range(6)]


def run_cycle():
    global X, cycle
    row = (cycle-1) // 40
    column = (cycle-1) % 40
    if column in (X-1, X, X+1):
        crt[row][column] = '#'
    if cycle == 20 or (20+cycle) % 40 == 0:
        segments.append(X*cycle)
    cycle += 1


while i < len(ops):
    op = ops[i]
    if "add" in op:
        last_val = int(op.split(" ")[1])
        for k in range(2):
            run_cycle()
            if k == 1:
                X += last_val
    else:
        run_cycle()

    i += 1

print(sum(segments))
for row in crt:
    print(''.join(row))
# submit(answer="RGZEHURK", level=2)
