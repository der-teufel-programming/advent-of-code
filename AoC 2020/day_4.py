import sys, re
with open(sys.argv[1], "r") as f:
    data = f.read().split("\n\n")

def valid(passp):
    p = dict([x.split(":") for x in passp.strip().split()])
    for e in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if e not in p: return False
    return True
 
def part1(data):
    return sum(map(valid, data))

print(part1(data))

def valid2(passp):
    p = dict([x.split(":") for x in passp.strip().split()])
    if "byr" not in p: return False
    elif len(p["byr"]) != 4 or (q := int(p["byr"])) < 1920 or q > 2002: return False
    if "iyr" not in p: return False
    elif len(p["iyr"]) != 4 or (q := int(p["iyr"])) < 2010 or q > 2020: return False
    if "eyr" not in p: return False
    elif len(p["eyr"]) != 4 or (q := int(p["eyr"])) < 2020 or q > 2030: return False
    if "hgt" not in p: return False
    else:
        if p["hgt"][-2:] == "cm":
            if (q := int(p["hgt"][:-2])) < 150 or q > 193: return False
        elif p["hgt"][-2:] == "in":
            if (q := int(p["hgt"][:-2])) < 59 or q > 76: return False
        else: return False
    if "hcl" not in p: return False
    elif not re.match("^#[0-9a-f]{6,6}$", p["hcl"]): return False
    if "ecl" not in p: return False
    elif p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False
    if "pid" not in p: return False
    elif not re.match("^[0-9]{9,9}$", p["pid"]): return False
    return True
 
def part2(data):
    return sum(map(valid2, data))

print(part2(data))