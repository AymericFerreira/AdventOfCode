import pathlib
from utils.post_answer import submit_solution


def contains(a, b):
    a = list(map(int, a.split("-")))
    b = list(map(int, b.split("-")))
    if a[0] <= b[0] and a[1] >= b[1] >= a[0]:
        return True
    if b[0] <= a[0] and b[1] >= a[1] >= b[0]:
        return True
    return False


def contains2(a, b):
    a = list(map(int, a.split("-")))
    b = list(map(int, b.split("-")))
    if a[0] <= b[0] <= a[1]:
        return True
    if b[0] <= a[0] <= b[1]:
        return True
    return False


def part_1(input: str):
    lines = input.splitlines()
    fully_contained = 0
    for line in lines:
        elf1 = line.split(",")[0]
        elf2 = line.split(",")[1]
        if contains(elf1, elf2) is True:
            fully_contained += 1
    return fully_contained


def part_2(input: str):
    lines = input.splitlines()
    fully_contained = 0
    for line in lines:
        elf1 = line.split(",")[0]
        elf2 = line.split(",")[1]
        if contains2(elf1, elf2) is True:
            fully_contained += 1
    return fully_contained


def submit_solution_part_1():
    submit_solution(part_1, 1)


def submit_solution_part_2():
    submit_solution(part_2, 1)


if __name__ == '__main__':
    input_content = pathlib.Path("input.txt").read_text()
    # print(part_1(input_content))
    print(part_2(input_content))
    # submit_solution_part_1()
    # submit_solution_part_2()
