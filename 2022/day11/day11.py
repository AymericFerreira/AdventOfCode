import pathlib
import re

import numpy as np

from utils.post_answer import submit_solution


class Monkey:
    def __init__(self, name):
        self.number = None
        self.monkey_if_false = None
        self.monkey_if_true = None
        self.test_number = None
        self.name = name
        self.operation = None
        self.items = []
        self.inspected_item = 0

    def add_operation(self, operation, number=None):
        self.operation = operation
        if operation == "old * old":
            # self.number = None
            pass
        else:
            self.number = number

    def perform_operation(self, item):
        if self.operation == "+":
            return item + self.number
        if self.operation == "*":
            return item * self.number
        if self.operation == "old * old":
            return item * item

    def add_item(self, number):
        self.items.append(number)
        # print(self.name, self.items)

    def add_test(self, number, monkey_true: float, monkey_false: float):
        self.test_number = number
        self.monkey_if_true = monkey_true
        self.monkey_if_false = monkey_false

    def test_item(self, item):
        operation_result = self.perform_operation(item)
        result = int(operation_result / 3)
        # print("item", item, " operation ", self.operation, " operation result ", operation_result, "result ", result)

        self.items.remove(item)
        # print(f"remove {item} from {self.name}")
        if result % self.test_number == 0:
            return result, self.monkey_if_true
        else:
            return result, self.monkey_if_false

    def process_list(self):
        return_list = []
        # print("self items ", self.items)
        item_list = self.items.copy()
        for item in item_list:
            number, monkey = self.test_item(item)
            self.inspected_item += 1
            # print(item, number, monkey)
            return_list.append({monkey: number})
        # print("return list ", return_list)
        return return_list


class Monkey2:
    def __init__(self, name):
        self.number = None
        self.monkey_if_false = None
        self.monkey_if_true = None
        self.test_number = None
        self.name = name
        self.operation = None
        self.items = []
        self.inspected_item = 0
        self.modulo = 1

    def modify_modulo(self, modulo):
        self.modulo = modulo

    def add_operation(self, operation, number=None):
        self.operation = operation
        if operation == "old * old":
            # self.number = None
            pass
        else:
            self.number = number

    def perform_operation(self, item):
        if self.operation == "+":
            return item + self.number
        if self.operation == "*":
            return item * self.number
        if self.operation == "old * old":
            return item * item

    def add_item(self, number):
        self.items.append(number)
        # print(self.name, self.items)

    def add_test(self, number, monkey_true: float, monkey_false: float):
        self.test_number = number
        self.monkey_if_true = monkey_true
        self.monkey_if_false = monkey_false

    def test_item(self, item):
        operation_result = self.perform_operation(item)
        result = int(operation_result % self.modulo)
        # print("item", item, " operation ", self.operation, " operation result ", operation_result, "result ", result)

        self.items.remove(item)
        # print(f"remove {item} from {self.name}")
        if result % self.test_number == 0:
            return result, self.monkey_if_true
        else:
            return result, self.monkey_if_false

    def process_list(self):
        return_list = []
        # print("self items ", self.items)
        item_list = self.items.copy()
        for item in item_list:
            number, monkey = self.test_item(item)
            self.inspected_item += 1
            # print(item, number, monkey)
            return_list.append({monkey: number})
        # print("return list ", return_list)
        return return_list


def parser(input: str):
    monkeyDict = {}
    actual_monkey = 0

    for line in input.splitlines():
        if "Monkey" in line:
            monkey_number = int(line.split(" ")[1][0])
            monkeyDict[monkey_number] = Monkey(monkey_number)
            actual_monkey = monkey_number
        elif "Starting items" in line:
            items = re.findall(r'\d+', line)
            for item in items:
                monkeyDict[actual_monkey].add_item(int(item))
        elif "Operation" in line:
            number = re.findall(r'\d+', line)
            if "old * old" in line:
                monkeyDict[actual_monkey].add_operation("old * old")
            elif "*" in line:
                monkeyDict[actual_monkey].add_operation("*", int(number[0]))
            elif "+" in line:
                monkeyDict[actual_monkey].add_operation("+", int(number[0]))
        elif "Test" in line:
            test_number = int(line.split(" ")[-1])
        elif "If true" in line:
            if_true = int(line.split(" ")[-1])
        elif "If false" in line:
            if_false = int(line.split(" ")[-1])

            monkeyDict[actual_monkey].add_test(test_number, if_true, if_false)

    return monkeyDict


def parser2(input: str):
    monkeyDict = {}
    actual_monkey = 0

    for line in input.splitlines():
        if "Monkey" in line:
            monkey_number = int(line.split(" ")[1][0])
            monkeyDict[monkey_number] = Monkey2(monkey_number)
            actual_monkey = monkey_number
        elif "Starting items" in line:
            items = re.findall(r'\d+', line)
            for item in items:
                monkeyDict[actual_monkey].add_item(int(item))
        elif "Operation" in line:
            number = re.findall(r'\d+', line)
            if "old * old" in line:
                monkeyDict[actual_monkey].add_operation("old * old")
            elif "*" in line:
                monkeyDict[actual_monkey].add_operation("*", int(number[0]))
            elif "+" in line:
                monkeyDict[actual_monkey].add_operation("+", int(number[0]))
        elif "Test" in line:
            test_number = int(line.split(" ")[-1])
        elif "If true" in line:
            if_true = int(line.split(" ")[-1])
        elif "If false" in line:
            if_false = int(line.split(" ")[-1])

            monkeyDict[actual_monkey].add_test(test_number, if_true, if_false)

    return monkeyDict


def part_1(input: str):
    monkey_dict = parser(input)
    for round in range(20):
        print("round ", round)
        for monkey in monkey_dict:
            throw_list = monkey_dict[monkey].process_list()
            for item in throw_list:
                for key, val in item.items():
                    monkey_dict[key].add_item(val)
                # monkey_dict[].add_item(item[1])
            # for monkey_number, item in throw_list:
            #     print(monkey_number, item)
            #     monkey_dict[monkey_number].add_item(item)
        # for monkey in monkey_dict:
        #     print(monkey_dict[monkey].items)
    monkey_business = []
    for monkey in monkey_dict:
        monkey_business.append(monkey_dict[monkey].inspected_item)
    return np.multiply(*sorted(monkey_business, reverse=True)[:2])
    # pass


def part_2(input: str):
    modulo = 1
    monkey_dict = parser2(input)
    for monkey in monkey_dict:
        modulo *= monkey_dict[monkey].test_number
        print(modulo)
    for monkey in monkey_dict:
        monkey_dict[monkey].modify_modulo(modulo)
    # exit()
    for round in range(10000):
        print("round ", round)
        for monkey in monkey_dict:
            throw_list = monkey_dict[monkey].process_list()
            for item in throw_list:
                for key, val in item.items():
                    monkey_dict[key].add_item(val)
                # monkey_dict[].add_item(item[1])
            # for monkey_number, item in throw_list:
            #     print(monkey_number, item)

            #     monkey_dict[monkey_number].add_item(item)
        # for monkey in monkey_dict:
        #     print(monkey_dict[monkey].items)
    monkey_business = []
    for monkey in monkey_dict:
        monkey_business.append(monkey_dict[monkey].inspected_item)
    print(monkey_business)
    # Because of overflow error we need to convert to int64
    return np.multiply(*sorted(np.array(monkey_business).astype(np.int64), reverse=True)[:2])
    # pass


def submit_solution_part_1():
    submit_solution(part_1, 1)


def submit_solution_part_2():
    submit_solution(part_2, 1)


if __name__ == '__main__':
    input_content = pathlib.Path("input.txt").read_text()
    a = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    # print(part_1(a))
    # print(part_1(input_content))
    # print(part_2(a))
    print(part_2(input_content))
    # ))
    # submit_solution_part_1()
    # submit_solution_part_2()
