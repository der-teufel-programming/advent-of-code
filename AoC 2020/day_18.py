import sys, operator
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n")

ops = {'+' : operator.add, '*' : operator.mul}
def calc(s, prec):
    s, op = s.replace(' ', ''), []
    curr = ''
    for c in s:
        if c in '0123456789.': curr += c
        else:
            if curr: op.append(int(curr))
            if c != ' ': op.append(c)
            curr = ''
    if curr: op.append(int(curr))
    rpn, ope = [], []
    for e in op:
        if type(e) == int: rpn.append(e)
        else:
            if e == '(': ope.append(e)
            elif e == ')':
                while ope[-1] != '(': rpn.append(ope.pop())
                ope.pop()
            else:
                if len(ope) == 0: ope.append(e)
                else:
                    if prec[e] > prec[ope[-1]]: ope.append(e)
                    elif prec[e] < prec[ope[-1]]:
                        while len(ope) > 0 and prec[e] <= prec[ope[-1]]: rpn.append(ope.pop())
                        ope.append(e)
                    elif prec[e] == prec[ope[-1]]:
                        while len(ope) > 0 and prec[e] <= prec[ope[-1]]: rpn.append(ope.pop())
                        ope.append(e)
    while len(ope) > 0: rpn.append(ope.pop())
    for x in rpn:
        if str(x) in '+*':
            b, a = ope.pop(), ope.pop()
            ope.append(ops[x](a, b))
        else: ope.append(x)       
    return ope[-1]

def part1(equations):
    def c(eq):
        return calc(eq, {'+' : 1, '*' : 1, '(' : -1})
    return sum(map(c, equations))

def part2(equations):
    def c(eq):
        return calc(eq, {'+' : 1, '*' : 0, '(' : -1})
    return sum(map(c, equations))

print(part1(data))
print(part2(data))