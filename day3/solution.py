def get_priority(letter):

    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

with open("day3/input.txt", "r") as f:
    input = f.read()

rucksacks = input.split("\n")

compartments = [[r[:int(len(r)/2)], r[int(len(r)/2):]] for r in rucksacks]

total = 0

for rucksack in compartments:
    a, b = map(lambda x: set(x), rucksack)
    common_items = list(a & b)
    priorities = [get_priority(x) for x in common_items]
    total += sum(priorities)

print(total)