import re
import numpy as np
from  aoc_template import submit, prepare_day, read_file_to_str

def part_1(data: str) -> int:
    left_coordinate, right_coordinate = parser(data)
    return sum(abs(np.array(left_coordinate) - np.array(right_coordinate)))

def part_2(data: str) -> int:
    left_coordinate, right_coordinate = parser(data)
    return sum(left * right_coordinate.count(left) for left in left_coordinate)

def parser(data: str) -> ([int], [int]):
    position_list = re.findall(r'\d+', data)
    left_coordinate = list(map(int, position_list[::2]))
    right_coordinate = list(map(int, position_list[1::2]))
    return sorted(left_coordinate), sorted(right_coordinate)


example = """3   4
4   3
2   5
1   3
3   9
3   3"""
if __name__ == '__main__':
    # prepare_day(__file__)
    # submit(2024, 1, part_1(read_file_to_str(__file__)))
    submit(2024, 1, part_2(read_file_to_str(__file__)))