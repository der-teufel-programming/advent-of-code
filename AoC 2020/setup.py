import sys, aocd
year, day = sys.argv[1], sys.argv[2]
print(day)
with open("template.py", "r") as template:
    with open(f"day_{day}.py", "a") as f:
        f.write(template.read())
print(f"Created `day_{day}.py`")
with open(f"day_{day}_data.txt", "w") as f:
    f.write(aocd.get_data(day=int(day), year=int(year)))
print(f"Created `day_{day}_data.txt`")