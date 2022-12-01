puzzle_input = open("input.txt").read().split("\n\n")

elf_inventory = []

for inventory in puzzle_input:
    sum_inv = 0
    for item in inventory.split("\n"):
        if item:
            sum_inv += int(item)
    elf_inventory.append(sum_inv)

print(max(elf_inventory))
print(sum(sorted(elf_inventory, reverse=True)[:3]))
