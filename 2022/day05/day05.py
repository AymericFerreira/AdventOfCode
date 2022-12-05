import pathlib
import re

from utils.post_answer import submit_solution


class Crate:
    def __init__(self, id: int):
        self.containers = []
        self.id = id

    def add_container(self, new_containers):
        self.containers.extend(new_containers)

    def reverse_container(self):
        self.containers.reverse()


def generate_crates(number: 9):
    crates = {}
    for i in range(number):
        crates[i+1] = Crate(i+1)
    return crates


def parse_instruction(instruction: str):
    return list(map(int, re.findall(r"\d+", instruction)))


def part_1(input: str):
    crates = generate_crates(9)
    containers = input.splitlines()[:8]
    instructions = input.splitlines()[10:]
    for line in containers:
        letters = line[1::4]
        for crateIndex, letter in enumerate(letters):
            if letter != " ":
                crates[crateIndex + 1].add_container(letter)
    for crate in crates.values():
        crate.reverse_container()

    for instruction in instructions:
        number_to_move, origin, destination = parse_instruction(instruction)
        displacement = crates[origin].containers[-number_to_move:]
        displacement.reverse()
        crates[origin].containers = crates[origin].containers[:-number_to_move]
        crates[destination].containers += displacement
    answer = []
    for crate in crates.values():
        answer.append(crate.containers[-1])

    return "".join(answer)


def part_2(input: str):
    crates = generate_crates(9)
    containers = input.splitlines()[:8]
    instructions = input.splitlines()[10:]
    for line in containers:
        letters = line[1::4]
        for crateIndex, letter in enumerate(letters):
            if letter != " ":
                crates[crateIndex + 1].add_container(letter)
    for crate in crates.values():
        crate.reverse_container()

    for instruction in instructions:
        number_to_move, origin, destination = parse_instruction(instruction)
        displacement = crates[origin].containers[-number_to_move:]
        if number_to_move < 2:
            displacement.reverse()
        crates[origin].containers = crates[origin].containers[:-number_to_move]
        crates[destination].containers += displacement
    answer = []
    for crate in crates.values():
        answer.append(crate.containers[-1])

    return "".join(answer)


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
