import requests as r
from functools import reduce

with open("day1/input.txt") as f:
    input = f.read()

elves = input.strip().split('\n\n')

total_cals = []

for elf in elves:
    calories = elf.split('\n')
    total_cal = int(reduce(lambda a,b: int(a) + int(b), calories))
    total_cals.append(total_cal)

total_cals.sort(reverse=True)
print(reduce(lambda a,b: a + b, total_cals[:3]))