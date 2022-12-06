import pathlib
from utils.post_answer import submit_solution


def part_1(input: str):
    lines = input.splitlines()
    line = lines[0]
    return find_marker(line, 4)


def find_marker(line: str, number: int):
    for i in range(len(line)):
        marker = line[i - number:i]
        if len(set(marker)) == number:
            return i


def part_2(input: str):
    lines = input.splitlines()
    line = lines[0]
    return find_marker(line, 14)


def submit_solution_part_1():
    submit_solution(part_1, 1)


def submit_solution_part_2():
    submit_solution(part_2, 1)


if __name__ == '__main__':
    input_content = pathlib.Path("input.txt").read_text()
    print(part_1(input_content))
    print(part_2(input_content))
    # submit_solution_part_1()
    # submit_solution_part_2()
