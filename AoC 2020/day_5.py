import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

IDs = list(map(lambda x: int(x.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2), data))

part1 = max

print(part1(IDs))

def part2(ids):
    ids.sort()
    for ind, i in enumerate(ids):
        if ids[ind + 1] != i + 1:  return i + 1

print(part2(IDs))