import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

def parse_line(line):
    container, containees = line[:-1].split("contain")
    containees = [x.split(maxsplit=1)[1].strip() for x in containees.split(',')]
    containees = [x if x[-1] != 's' else x[:-1] for x in containees]
    return containees, container.strip()[:-1]
 
def part1(bags):
    bags_parse = list(map(parse_line, bags))
    baggage = dict()
    for e in bags_parse:
        for containee in e[0]:
            if containee not in baggage: baggage[containee] = set()
            baggage[containee].add(e[1])
    visited = set()
    to_visit = []
    to_visit += baggage['shiny gold bag']
    while len(to_visit) > 0:
        tmp = []
        for e in to_visit:
            if e in baggage:
                for k in baggage[e]:
                    if k not in visited: tmp.append(k)
            visited.add(e)
        to_visit = tmp
    return len(visited)

print(part1(data))

def parse_line_2(line):
    things = [x.strip() for x in line[:-1].split('contain')]
    things[1] = [x.strip() for x in things[1].split(',')]
    things[0] = things[0][:-1]
    things[1] = [x.split(maxsplit=1) for x in things[1]]
    things[1] = [(x, y if y[-1] != 's' else y[:-1]) for x,y in things[1]]
    return things
 
def packing(bag, multiplier, baggage_package):
    packed = 0
    if baggage_package[bag][0][0] == 'no': return 0
    packed += sum(int(x[0]) for x in baggage_package[bag])
    packed += sum(packing(bagn, count, baggage_package) for count, bagn in baggage_package[bag])
    return int(multiplier)*packed
 
def part2(bags):
    bags_parse = list(map(parse_line_2, bags))
    baggage = dict()
    for e in bags_parse:
        baggage[e[0]] = e[1]
    return packing('shiny gold bag', 1, baggage)

print(part2(data))