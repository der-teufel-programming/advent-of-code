import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

numbers = list(map(int, data))

def part1(numbers):
    for i, e in enumerate(numbers):
        for e1 in numbers[:i] + numbers[i+1:]:
            if e + e1 == 2020:
                return (e, e1, e*e1)

print(part1(numbers))

def part2(numbers):
    for i, x in enumerate(numbers):
        for y in numbers[:i] + numbers[i+1:]:
            if 2020 - x - y in numbers:
                return (x, y, 2020-x-y, x*y*(2020-x-y))

print(part2(numbers))