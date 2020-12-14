import sys
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

docking_prog = [line.split(' = ') for line in data]

def masks(mask):
    return [int(x, 2) for x in [mask.replace('X', '0'), mask.replace('X', '1')]]

def apply_mask(number, mask):
    mask = masks(mask)
    return (number|mask[0])&mask[1]

def part1(instrs):
    memory, mask = dict(), ''
    for instr in instrs:
        if instr[0] == 'mask':
            mask = instr[1]
        else:
            addr = instr[0].split('[')[1].split(']')[0]
            memory[addr] = apply_mask(int(instr[1]), mask)
    return sum(memory.values())

print(part1(docking_prog))

def address_mask(addr, mask):
    addr = bin(addr)[2:]
    addr = list('0' * (len(mask) - len(addr)) + addr)
    mask = list(mask)
    results = ['']
    for pair in zip(addr, mask):
        if pair[1] == '0': results = list(map(lambda x: x + pair[0], results))
        elif pair[1] == '1':  results = list(map(lambda x: x + '1', results))
        else: results = list(map(lambda x: x + '1', results)) + list(map(lambda x: x + '0', results))
    return results


def part2(instrs):
    memory, mask = dict(), ''
    for instr in instrs:
        if instr[0] == 'mask':
            mask = instr[1]
        else:
            addr = instr[0].split('[')[1].split(']')[0]
            for addr in address_mask(int(addr), mask): memory[addr] = int(instr[1])
    return sum(memory.values())

print(part2(docking_prog))