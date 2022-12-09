with open("input.txt") as inp:
    i = inp.read()


def get_sectors(sector_range):
    range_start, range_end = sector_range.split('-')

    range_start = int(range_start)
    range_end = int(range_end)

    range_list = []
    for x in range(range_start, range_end + 1):
        range_list.append(x)

    return range_list


subsets = 0
overlaps = 0
for pairs in i.splitlines():
    elf1, elf2 = pairs.split(",")

    elf1 = set(get_sectors(elf1))
    elf2 = set(get_sectors(elf2))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        subsets += 1

    if elf1.intersection(elf2):
        overlaps += 1

# part 1
print(subsets)

# part 2
print(overlaps)

