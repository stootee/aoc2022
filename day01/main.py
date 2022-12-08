with open("input.py") as inp:
    i = inp.read()

elves = []
this_elf = 0
for x in i.splitlines():
    if x:
        this_elf += int(x)

    else:
        elves.append(this_elf)
        this_elf = 0

# part1
print(max(elves))

# part2
p2_elves = []
for x in range(3):
    p2_elves.append(elves.pop(elves.index(max(elves))))

print(sum(p2_elves))