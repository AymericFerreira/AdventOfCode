import re
import numpy as np
from  aoc_template import submit, prepare_day, read_file_to_str
from benchmarking import FunctionBenchmark
import time

def check_if_sorted(array: [int]) -> bool:
    return sorted(array) == array or sorted(array, reverse=True) == array


def check_if_jump_is_safe(array: [int]) -> bool:
    sorted_array = sorted(array, reverse=True)
    for num1, num2 in zip(sorted_array, sorted_array[1:]):
        if num1 - num2 > 3:
            return False
        if num1 == num2:
            return False
    return True


def check_if_level_is_safe(array: [int]) -> bool:
    return check_if_sorted(array) and check_if_jump_is_safe(array)


def part_1(levels: [[int]]) -> int:
    return sum(int(check_if_level_is_safe(level)) for level in levels)


def remove_a_level(array: [int], position: int) -> [int]:
    del array[position]
    return array

def check_with_less_levels(level: [int]) -> bool:
    for i in range(len(level)):
        smaller_level = level.copy()
        smaller_level = remove_a_level(smaller_level, i)
        if check_if_level_is_safe(smaller_level):
            return True
    return False

def part_2(levels: [[int]]) -> int:
    safe_levels = 0
    for level in levels:
        if check_if_level_is_safe(level):
            safe_levels += 1
        elif check_with_less_levels(level):
            safe_levels += 1

    return safe_levels

def parser(data: str) -> [int]:
    return [
        list(map(int, re.findall(r"(\d+)", level)))
        for level in data.splitlines()
    ]


example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

if __name__ == '__main__':
    # prepare_day(__file__)
    # print(part_1(parser(example)))
    # print(part_1(parser(read_file_to_str(__file__))))
    # submit(2024, 2, part_1(parser(read_file_to_str(__file__))))
    print(part_2(parser(example)))
    # print(part_2(parser(read_file_to_str(__file__))))
    # submit(2024, 2, part_2(parser(read_file_to_str(__file__))))
    # content = read_file_to_str(__file__)
