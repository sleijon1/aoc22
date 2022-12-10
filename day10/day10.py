from aocutils.clients.client import fetch, submit

fetch()

ops = open("day10/input.txt").read().splitlines()

X, last_val = 1, 0
segments = []
cycle, i = 1, 0
crt = [['.' for _ in range(40)] for _ in range(6)]
while i < len(ops):
    op = ops[i]
    if "add" in op:
        last_val = int(op.split(" ")[1])
        for k in range(2):
            row = (cycle-1) // 40
            column = (cycle-1) % 40
            if column in (X-1, X, X+1):
                draw = '#'
            else:
                draw = '.'
            print(draw, row, column, X)
            cycle += 1
            crt[row][column] = draw
            if k == 1:
                X += last_val
            if cycle == 20 or (20+cycle) % 40 == 0:
                segments.append(X*cycle)
    else:
        row = (cycle-1) // 40
        column = (cycle-1) % 40
        if column in (X-1, X, X+1):
            draw = '#'
        else:
            draw = '.'
        cycle += 1
        crt[row][column] = draw
        if (cycle == 20 or (20+cycle) % 40 == 0):
            segments.append(X*(cycle))

    i += 1


print(X)
print(segments)
print(sum(segments))
for row in crt:
    print(''.join(row))
#submit(answer=sum(segments))
submit(answer="RGZEHURK", level=2)
