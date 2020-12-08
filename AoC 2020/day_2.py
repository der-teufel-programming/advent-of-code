import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

passwords = list(map(lambda x: (x[0].split(), x[1]), map(lambda x: x.split(': '), data)))

def good(password):
    counts = [int(x) for x in password[0][0].split('-')]
    return password[1].count(password[0][1]) in range(counts[0], counts[1] + 1)

def part1(passwords):
    return sum(map(good, passwords))

def good2(password):
    index = [int(x) for x in password[0][0].split('-')]
    return (password[1][index[0] - 1] == password[0][1]) ^ (password[1][index[1] - 1] == password[0][1])

def part2(passwords):
    return sum(map(good2, passwords))

print(part1(passwords))
print(part2(passwords))