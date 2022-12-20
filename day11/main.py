# from example import Monkey0, Monkey1, Monkey2, Monkey3
from input import *
import math


class Monkey:

    inspected = 0

    def __init__(self, input: dict):
        self.items = input['items']
        self.test = input['test']
        self.true = input['true']
        self.false = input['false']
        self.operation = input['operation'].split(" ")

    def monkey_test(self, part1=True):

        for i in range(len(self.items)):
            item = self.items.pop(0)
            # print(item)

            operation_value = self.operation[4]
            if operation_value == 'old':
                operation_value = item

            operation = '%s %s %s' % (item, self.operation[3], operation_value)
            # print(operation)
            new_worry = eval(operation)
            if part1:
                new_worry = math.floor(new_worry / 3)

            pass_command = "%s.receive(%s)"
            if new_worry % self.test == 0:
                pass_command = pass_command % (self.true, new_worry)
            else:
                pass_command = pass_command % (self.false, new_worry)

            # print(pass_command)
            eval(pass_command)

            self.inspected += 1

    def receive(self, item):
        self.items.append(item)


m0 = Monkey(Monkey0)
m1 = Monkey(Monkey1)
m2 = Monkey(Monkey2)
m3 = Monkey(Monkey3)
m4 = Monkey(Monkey4)
m5 = Monkey(Monkey5)
m6 = Monkey(Monkey6)
m7 = Monkey(Monkey7)

round = 0
while round < 10000:
    for m in [
        m0,
        m1,
        m2,
        m3,
        m4,
        m5,
        m6,
        m7,
    ]:

        m.monkey_test(False)
        # print(m.items)

    round += 1

    if round % 10 == 0:
        print(round)

for m in [
    m0,
    m1,
    m2,
    m3,
    m4,
    m5,
    m6,
    m7,
]:
    print(m, m.inspected)