from termcolor import colored

with open("input.txt") as inp:
    i = inp.read()

# i = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop"""

# i = """noop
# addx 3
# addx -5"""

command_cycles = {
    'addx': 2,
    'noop': 1
}


cycle = 0
register = 1
step = 20
signals = {}
signal_strength = 0

sprite_cycle = 0
sprite_position = {}
sprite = [0, 1, 2]



for commands in i.splitlines():
    command = commands.split(' ')

    if len(command) > 1:
        command, value = command
    else:
        command = command[0]
        value = None

    for _sc in range(command_cycles[command]):
        sprite_position[str(cycle + _sc + 1)] = [register, register + 1, register + 2]

    cycle += command_cycles[command]

    increment_step = False

    if cycle >= step:
        signal_strength = register

        increment_step = True

    if value:
        register += int(value)

    if increment_step:
        signals[str(step)] = signal_strength * step
        step += 40

#  part 1
print(sum(signals.values()))

# part 2
sprite_left = 0
# print(sprite_position)
for k, v in sprite_position.items():
    if int(k) - sprite_left in v:
        print('#', end='')
    else:
        print(' ', end='')

    if int(k) % 40 == 0:
        sprite_left += 40
        print()

