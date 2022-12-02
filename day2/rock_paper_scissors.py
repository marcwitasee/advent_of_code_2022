"""
A (Rock)
B (Paper)
C (Scissors)

X (Rock)
Y (Paper)
Z (Scissors)

A:
    A draws with X (3)
    A loses to Y (0)
    A beats Z (6)

B:
    B beats X (6)
    B draws Y (3)
    B loses to Z (0)

C:
    C loses to X (0)
    C beats Y (6)
    C draws Z (3)
"""


with open("day2/input.txt") as f:
    input = f.read()

shape_point_map = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

shape_map = {
    "A": ord("R"),
    "B": ord("P"),
    "C": ord("S"),
    "X": ord("R"),
    "Y": ord("P"),
    "Z": ord("S")
}

result_map = {
    -3: 6,
    -2: 0,
    -1: 0,
    0: 3,
    1: 6,
    2: 6,
    3: 0
}

def get_round_points(opp, me):

    opp_shape = shape_map[opp]
    me_shape = shape_map[me]
    result = opp_shape - me_shape

    return result_map[result]
    

rounds =  input.split("\n")
point_total = 0
for round in rounds:
    opp, me = round.split(' ')
    point_total += shape_point_map[me]
    point_total += get_round_points(opp, me)

print(point_total)
