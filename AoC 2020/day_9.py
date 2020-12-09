import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

numbers = list(map(int, data))

def insum(num, numbers):
    for i, x in enumerate(numbers):
        for y in numbers[:i] + numbers[i+1:]:
            if x + y == num: return True
    return False

def part1(nums):
    for i, e in enumerate(nums[25:]):
        if not insum(e, nums[i:i+25]): return e

print(part1(numbers))

def part2(nums):
    invalid = part1(numbers)
    i, j = 0, 0
    while (s := sum(nums[i:j+1])) != invalid:
        if s < invalid: j += 1
        elif s > invalid: i += 1
    return min(nums[i:j+1]) + max(nums[i:j+1])

print(part2(numbers))