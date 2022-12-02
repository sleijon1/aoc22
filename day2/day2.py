lines = open("input.txt").readlines()

opposites = {"Y": "A", "Z": "B", "X": "C"}
same = {"Y": "B", "Z": "C", "X": "A"}
type_point = {"Y": 2, "Z": 3, "X": 1}
regular_game = {"B": "A", "A": "C", "C": "B"}
regular_game_flipped = {val: key for key, val in regular_game.items()}
type_point_reg = {"B": 2, "C": 3, "A": 1}

score = 0
score_2 = 0
for line in lines:
    opponent, me = [x.strip() for x in line.split(" ")]
    score += type_point[me]
    if opposites[me] == opponent:
        score += 6
    elif opponent == same[me]:
        score += 3
    if me == "X":
        score_2 += type_point_reg[regular_game[opponent]]
    elif me == "Y":
        score_2 += type_point_reg[opponent]
        score_2 += 3
    else:
        score_2 += type_point_reg[regular_game_flipped[opponent]]
        score_2 += 6

print(score)
print(score_2)