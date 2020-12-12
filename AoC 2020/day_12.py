import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

instrs = list(map(lambda x: (x[0], x[1:]), data))

def part1(directions):
    pos = 0+0j
    dir = 1
    for e, num in directions:
        if e == 'N': pos += 0+int(num)*1j
        elif e == 'S': pos -= 0+int(num)*1j
        elif e == 'E': pos += int(num)+0j
        elif e == 'W': pos -= int(num)+0j
        elif e == 'F': pos += dir*int(num)
        elif e == 'L': dir *= {90:1j, 180:-1, 270:-1j}.get(int(num))
        elif e == 'R': dir *= {90:-1j, 180:-1, 270:1j}.get(int(num))
    return int(abs(pos.real)+abs(pos.imag))

print(part1(instrs))

def part2(directions):
    pos, way = 0+0j, 10+1j
    for e, num in directions:
        if e == 'N': way += 0+int(num)*1j
        elif e == 'S': way -= 0+int(num)*1j
        elif e == 'E': way += int(num)+0j
        elif e == 'W': way -= int(num)+0j
        elif e == 'F': pos += int(num)*way
        elif e == 'L': way *= {90:1j, 180:-1, 270:-1j}.get(int(num))
        elif e == 'R': way *= {90:-1j, 180:-1, 270:1j}.get(int(num))
    return int(abs(pos.real)+abs(pos.imag))

print(part2(instrs))