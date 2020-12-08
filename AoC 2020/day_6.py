import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n\n")

def part1(groups):
    return sum(map(lambda group: len(set(group.replace('\n', ''))), groups))

print(part1(data))

def part2(groups):
    return sum(map(lambda group: sum([1 if group.count(x)==group.count('\n')+1 else 0 for x in set(group.replace('\n', ''))]), groups))

print(part2(data))