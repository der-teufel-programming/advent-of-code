import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

numbers = [int(x) for x in data[0].split(',')]

def part1(nums, limit=2020):
    was = dict()
    for i, e in enumerate(nums, 1):
        was[e] = i
    round = len(nums) + 1
    curr_num = 0
    while round < limit:
        if curr_num in was:
            next_num = round - was[curr_num]
        else:
            next_num = 0
        was[curr_num] = round
        curr_num = next_num
        round += 1
    return curr_num

print(part1(numbers))

def part2(nums, limit=30000000):
    return part1(nums, limit=limit)

print(part2(numbers))