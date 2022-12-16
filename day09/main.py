import numpy as np
import matplotlib.pyplot as plt

with open("input.txt") as inp:
    i = inp.read()

# i = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

# i = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""


class End:

    where_have_i_been = []

    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.where_have_i_been.append((x, y))

    def where_am_i(self):
        return self.x, self.y

    @staticmethod
    def reposition(position: tuple, movement: tuple):
        if not len(position) == 2:
            raise Exception

        if not len(movement) == 2:
            raise Exception

        return position[0] + movement[0], position[1] + movement[1]

    def where_i_have_been(self, position):
        if position not in self.where_have_i_been:
            self.where_have_i_been.append(position)

    def move_head(self, direction: str):
        position = self.reposition((self.x, self.y), self.directions[direction])
        self.x, self.y = position

        # self.where_i_have_been(self.where_am_i())

    def follow_head(self, head_position):
        tail_position = self.where_am_i()

        x_distance = head_position[0] - tail_position[0]
        y_distance = head_position[1] - tail_position[1]

        moved = True
        x_move = 0
        y_move = 0

        if abs(x_distance) > 1 and abs(y_distance) > 1:
            x_move = x_distance/abs(x_distance)
            y_move = y_distance/abs(y_distance)

        elif abs(x_distance) > 1:
            x_move = x_distance/abs(x_distance)
            y_move = y_distance

        elif abs(y_distance) > 1:
            x_move = x_distance
            y_move = y_distance / abs(y_distance)

        else:
            moved = False

        if moved:
            self.x += int(x_move)
            self.y += int(y_move)

            self.where_i_have_been(self.where_am_i())


class Rope:

    def __init__(self, x=0, y=0):
        self.head = End(x, y)
        self.tail = End(x, y)

    def follow(self, position):
        self.tail.follow_head(position)
        print(self.tail.where_am_i())

    def move(self, direction: str, count: int):
        for move in range(count):
            self.head.move_head(direction)

            self.follow(self.head.where_am_i())


rope = Rope()

# part1
for z in i.splitlines():
    mv, cnt = z.split(' ')
    rope.move(mv, int(cnt))

print(len(set(rope.tail.where_have_i_been)))

# Part 2

rope0 = Rope()
rope1 = Rope()
rope2 = Rope()
rope3 = Rope()
rope4 = Rope()
rope5 = Rope()
rope6 = Rope()
rope7 = Rope()
rope8 = Rope()
rope9 = Rope()

wheres_my_tail = []
for z in i.splitlines():
    mv, cnt = z.split(' ')
    for move in range(int(cnt)):
        rope0.head.move_head(mv)
        print('Head', rope0.head.where_am_i())
        rope0.follow(rope0.head.where_am_i())

        rope1.head.x, rope1.head.y = rope0.tail.where_am_i()
        rope1.follow(rope1.head.where_am_i())

        rope2.head.x, rope2.head.y = rope1.tail.where_am_i()
        rope2.follow(rope2.head.where_am_i())

        rope3.head.x, rope3.head.y = rope2.tail.where_am_i()
        rope3.follow(rope3.head.where_am_i())

        rope4.head.x, rope4.head.y = rope3.tail.where_am_i()
        rope4.follow(rope4.head.where_am_i())

        rope5.head.x, rope5.head.y = rope4.tail.where_am_i()
        rope5.follow(rope5.head.where_am_i())

        rope6.head.x, rope6.head.y = rope5.tail.where_am_i()
        rope6.follow(rope6.head.where_am_i())

        rope7.head.x, rope7.head.y = rope6.tail.where_am_i()
        rope7.follow(rope7.head.where_am_i())

        rope8.head.x, rope8.head.y = rope7.tail.where_am_i()
        rope8.follow(rope8.head.where_am_i())
        wheres_my_tail.append(rope8.tail.where_am_i())

        # rope9.head.x, rope9.head.y = rope8.tail.where_am_i()
        # rope9.follow(rope9.head.where_am_i())
        # wheres_my_tail.append(rope9.tail.where_am_i())

    X = np.array([
        rope0.head.where_am_i()[0],
        rope0.tail.where_am_i()[0],
        rope1.tail.where_am_i()[0],
        rope2.tail.where_am_i()[0],
        rope3.tail.where_am_i()[0],
        rope4.tail.where_am_i()[0],
        rope5.tail.where_am_i()[0],
        rope6.tail.where_am_i()[0],
        rope7.tail.where_am_i()[0],
        rope8.tail.where_am_i()[0],
        # rope9.tail.where_am_i()[0],
    ])

    Y = np.array([
        rope0.head.where_am_i()[0],
        rope0.tail.where_am_i()[1],
        rope1.tail.where_am_i()[1],
        rope2.tail.where_am_i()[1],
        rope3.tail.where_am_i()[1],
        rope4.tail.where_am_i()[1],
        rope5.tail.where_am_i()[1],
        rope6.tail.where_am_i()[1],
        rope7.tail.where_am_i()[1],
        rope8.tail.where_am_i()[1],
        # rope9.tail.where_am_i()[1],
    ])

    C = np.array([[0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 0, 0]])

    # plt.scatter(X, Y, c=C/255)
    # plt.show()

X = np.array([x for x, y in wheres_my_tail])
Y = np.array([y for x, y in wheres_my_tail])

# Plotting point using sactter method
plt.scatter(X, Y)
plt.show()
print(len(set(wheres_my_tail)))


