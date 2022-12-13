import hashlib
puzzle_input = open("2016 warmup/input.txt").read().strip()

def get_password(level):
    password = []
    i = 0
    while len(password) < 8:
        puzzle_hash = hashlib.md5((puzzle_input+str(i)).encode()).hexdigest()
        if puzzle_hash[:5] == "00000":
            try:
                if level == 2 and \
                    int(puzzle_hash[5]) > 7 or puzzle_hash[5] in [x[0] for x in password]:
                    pass
                else:
                    password.append((puzzle_hash[5], puzzle_hash[6]))
            except ValueError:
                pass
        i += 1
    return password

print("".join([x[0] for x in get_password(1)]))
sorted_pw = sorted(get_password(2), key=lambda x: x[0])
print("".join([x[1] for x in sorted_pw]))
