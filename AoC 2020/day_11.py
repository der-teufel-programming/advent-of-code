import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

def parse_layout(layout_text):
    parsed_l = dict()
    for y, row in enumerate(layout_text):
        for x, seat in enumerate(row):
            parsed_l[(y,x)] = seat
    return parsed_l

seats = parse_layout(data)

def get_neighbours(y, x, layout, height, width):
    if y > 0 and y < height - 1: rows = range(y - 1, y + 2)
    else: rows = range(0, 2) if y == 0 else range(height - 2, height)
    if x > 0 and x < width - 1: cols = range(x - 1, x + 2)
    else: cols = range(0, 2) if x == 0 else range(width - 2, width)
    neighbours = []
    for j in rows:
        for i in cols:
            if j != y or i != x: neighbours.append(layout[(j, i)])
    return neighbours

def part1(layout, height, width):
    l_copy, changed, steps = dict(), -1, 0
    while changed != 0:
        changed = 0
        steps += 1
        for y in range(height):
            for x in range(width):
                seat = layout[(y, x)]
                occu = sum(map(lambda n: 0 if n in 'L.' else 1, get_neighbours(y, x, layout, height, width)))
                if seat == '.':
                    l_copy[(y,x)] = '.'
                elif occu == 0 and seat == 'L':
                    l_copy[(y,x)] = '#'
                    changed += 1
                elif occu >= 4 and seat == '#':
                    l_copy[(y,x)] = 'L'
                    changed += 1
                else:
                    l_copy[(y,x)] = seat
        layout = l_copy.copy()
    s = 0
    for y in range(height):
        for x in range(width):
            s += (lambda n: 0 if n in 'L.' else 1)(layout[(y, x)])
    return s

print(part1(seats, len(data), len(data[0])))

def get_neighbours_2(y, x, layout, height, width):
    def add(p, d):
        return (p[0] + d[0], p[1] + d[1])
    def check_direction(start, direction, height, width):
        pos = add(start, direction)
        while 0 <= pos[1] and pos[1] < width and 0 <= pos[0] and pos[0] < height:
            if layout[pos] != '.': return layout[pos]
            pos = add(pos, direction)
        return '.'
    neighbours = [check_direction((y, x), dir, height, width) for dir in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]]
    return neighbours

def part2(layout, height, width):
    l_copy, changed, steps = dict(), -1, 0
    while changed != 0:
        changed = 0
        steps += 1
        for y in range(height):
            for x in range(width):
                seat = layout[(y, x)]
                occu = sum(map(lambda n: 0 if n in 'L.' else 1, get_neighbours_2(y, x, layout, height, width)))
                if seat == '.':
                    l_copy[(y,x)] = '.'
                elif occu == 0 and seat == 'L':
                    l_copy[(y,x)] = '#'
                    changed += 1
                elif occu >= 5 and seat == '#':
                    l_copy[(y,x)] = 'L'
                    changed += 1
                else:
                    l_copy[(y,x)] = seat
        layout = l_copy.copy()
    s = 0
    for y in range(height):
        for x in range(width):
            s += (lambda n: 0 if n in 'L.' else 1)(layout[(y, x)])
    return s

print(part2(seats, len(data), len(data[0])))