with open("input.py") as inp:
    i = inp.read()

# Part 1
moves = {
    "A": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0},
    "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "C": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3},
}

score = 0
for move in i.splitlines():
    p1, p2 = move.split()
    score += moves[p1][p2]

print(score)

# Part 2
moves = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}

scores = {"X": 0, "Y": 3, "Z": 6}

score = 0
for move in i.splitlines():
    p1, p2 = move.split()
    score += moves[p1][p2] + scores[p2]

print(score)
