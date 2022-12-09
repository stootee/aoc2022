with open("input.txt") as inp:
    i = inp.read()

# part 1
priority_score = 0
for rucksack in i.splitlines():
    items = list(rucksack)
    no_of_items = int(len(items) / 2)
    compartment1 = set(items[:no_of_items])
    compartment2 = set(items[no_of_items:])

    dupe = compartment1.intersection(compartment2).pop()

    if dupe == dupe.upper():
        score = ord(dupe) - 38
    else:
        score = ord(dupe) - 96

    priority_score += score

print(priority_score)

# part 2
group_cnt = 0
common_bag = set()
badge_score = 0
for rucksack in i.splitlines():
    this_bag = set(list(rucksack))

    if group_cnt == 0:
        common_bag = this_bag
    else:
        common_bag = common_bag.intersection(this_bag)

    if group_cnt == 2:
        badge = common_bag.pop()

        group_cnt = 0

        if badge == badge.upper():
            score = ord(badge) - 38
        else:
            score = ord(badge) - 96

        badge_score += score

    else:
        group_cnt += 1

print(badge_score)
