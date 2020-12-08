with open("day_8_data.txt", "r") as f:
    data = f.read().split("\n")

instrs = list(map(lambda x: (lambda y: (y[0], int(y[1])))(x.split()), data))

def part1_day8(codes):
    instrs, accu, pointer = [], 0, 0
    while True:
        if pointer in instrs: return accu
        instrs.append(pointer)
        if pointer > len(codes) - 1: return accu
        if codes[pointer][0] == "nop": pointer += 1
        elif codes[pointer][0] == "acc":
            accu += codes[pointer][1]
            pointer += 1
        elif codes[pointer][0] == "jmp": pointer += codes[pointer][1]

print(part1_day8(instrs))

def test_loop(code):
    used, pointer = [], 0
    while True:
        if pointer in used: return False
        used.append(pointer)
        if pointer > len(code) - 1: return True
        if code[pointer][0] in ["nop", "acc"]: pointer += 1
        else: pointer += code[pointer][1]

def find_loopless(data):
    for i, e in enumerate(data):
        if e[0] == "nop":
            data[i] = ("jmp", data[i][1])
            if test_loop(data): return i, e
            data[i] = ("nop", data[i][1])
        elif e[0] == "jmp":
            data[i] = ("nop", data[i][1])
            if test_loop(data): return i, e
            data[i] = ("jmp", data[i][1])

change = find_loopless(instrs)
instrs[change[0]] = ("nop" if change[1][0] == "jmp" else "jmp", change[1][1])
print(part1_day8(instrs))
