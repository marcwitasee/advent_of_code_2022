
with open("day2/input.txt") as f:
    input = f.read()

result_map = {
    5720: 3,
    5785: 4,
    5850: 8,
    5808: 1,
    5874: 5,
    5940: 9,
    5896: 2,
    5963: 6,
    6030: 7
}

def get_round_points(opp, outcome):

    result = ord(opp) * ord(outcome)

    return result_map[result]
    

rounds =  input.split("\n")
point_total = 0
for round in rounds:
    opp, outcome = round.split(' ')
    point_total += get_round_points(opp, outcome)

print(point_total)
