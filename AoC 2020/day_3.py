import sys
from functools import reduce
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

def part1(trees):
    x, y, count = 0, 0, 0
    while y < len(trees):
        if trees[y][x % len(trees[y])] == '#': count += 1
        x, y = x + 3, y + 1
    return count

print(part1(data))

def part2(trees):
    def slope(trees, dx, dy):
        x, y, count = 0, 0, 0
        while y < len(trees):
            if trees[y][x % len(trees[y])] == '#': count += 1
            x, y = x + dx, y + dy
        return count
    return reduce(lambda x, y: x*y, (slope(trees, dx, dy) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))

print(part2(data))