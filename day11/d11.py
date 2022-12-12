from aocutils.clients.client import fetch, submit
from collections import defaultdict


monkeys = open("day11/input.txt").read().split("\n\n")
monkeys = [[unstripped.strip() for unstripped in monkey.splitlines()] for monkey in monkeys]
parsed_monkeys = {}


def multiply(x, y):
    return x*y


def add(x, y):
    return x+y


def test(monkey_true, monkey_false, test, value):
    if value % test == 0:
        return monkey_true
    return monkey_false


def prep_monkeys():
    div_factor = 1
    for monkey in monkeys:
        parsed_monkeys[monkey[0]] = {}
        starting_items = monkey[1].split(": ")[1].split(', ')
        starting_items = [int(item) for i, item in enumerate(starting_items)]
        operation, value = monkey[2].split("old ")[1].split(" ")
        if operation == '*':
            operation = (multiply, value)
        else:
            operation = (add, value)
        divisible_by = int(monkey[3].split("by ")[-1])
        true = int(monkey[4].split("monkey ")[-1])
        false = int(monkey[5].split("monkey ")[-1])
        div_factor *= divisible_by

        parsed_monkeys[monkey[0]]['div_by'] = divisible_by
        parsed_monkeys[monkey[0]]['true'] = true
        parsed_monkeys[monkey[0]]['false'] = false
        parsed_monkeys[monkey[0]]['starting_items'] = starting_items
        parsed_monkeys[monkey[0]]['operation'] = operation
        parsed_monkeys[monkey[0]]['name'] = monkey[0]
    return div_factor, parsed_monkeys


def calc_monkey_business(a=True):
    inspections = defaultdict(int)
    rounds = 20 if a else 10000
    div_factor, parsed_monkeys = prep_monkeys()
    for _ in range(rounds):
        for _, monkey in parsed_monkeys.items():
            items = list(monkey['starting_items'])
            for item in items:
                inspections[monkey['name']] += 1
                op, val = monkey['operation']
                if val == "old":
                    item = op(item, item)
                else:
                    item = op(item, int(val))

                if a:
                    item //= 3
                # key
                item = item % div_factor
                recieve_monkey = test(monkey['true'], monkey['false'], monkey['div_by'], item)
                parsed_monkeys[f"Monkey {recieve_monkey}:"]['starting_items'].append(item)
                monkey['starting_items'].pop(0)

    sorted_ = sorted(inspections.values())
    return multiply(sorted_[-2], sorted_[-1])


monkey_business_a = calc_monkey_business(True)
print(monkey_business_a)
monkey_business_b = calc_monkey_business(False)
print(monkey_business_b)

#submit(answer=monkey_business_b, level=2)
