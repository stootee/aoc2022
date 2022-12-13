from day05.input import moves, crates
from copy import deepcopy

PILES = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
}
for x in crates.splitlines():
    for y in range(0, 9):
        pos = y * 4
        crate = x[pos + 1]

        if not crate.isspace() and not crate.isnumeric():
            PILES[str(y + 1)].insert(0, crate)

piles2 = deepcopy(PILES)


def move_crates(num_of_crates:int, from_pile:str, to_pile:str, new_crane=False):
    if not new_crane:
        for m in range(num_of_crates):
            crate = PILES[from_pile].pop()
            PILES[to_pile].append(crate)

    else:
        moved_crates = PILES[from_pile][-1 * num_of_crates:]
        print(moved_crates)
        PILES[from_pile] = PILES[from_pile][:len(PILES[from_pile]) - num_of_crates]
        PILES[to_pile] += moved_crates


for x in moves.splitlines():
    commands = x.split(" ")
    move_crates(int(commands[1]), commands[3], commands[5])

piles1 = deepcopy(PILES)
print(piles1)
for x in piles1:
    print(piles1[x][-1], end='')
print()

PILES = piles2.copy()
print(PILES)
for x in moves.splitlines():
    commands = x.split(" ")
    move_crates(int(commands[1]), commands[3], commands[5], True)

print(PILES)
for x in PILES:
    print(PILES[x][-1], end='')

