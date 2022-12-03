import pathlib
from utils.post_answer import submit_solution


def part_1(input: str):
    lines = input.splitlines()
    priority = 0
    for line in lines:
        compartment1 = set(line[:len(line)//2])
        compartment2 = set(line[len(line)//2:])
        letter = compartment1.intersection(compartment2)
        priority += convert_to_priority(letter)
    return priority


def convert_to_priority(char: set):
    if list(char)[0].isupper():
        priority = ord(list(char)[0]) - 64 + 26
    else:
        priority = ord(list(char)[0]) - 96
    return priority


def part_2(input: str):
    lines = input.splitlines()
    priority = 0
    for elf1, elf2, elf3 in \
            zip(lines[::3], lines[1::3], lines[2::3]):
        compartment = set(elf1).intersection(set(elf2)).intersection(set(elf3))
        priority += convert_to_priority(compartment)
    return priority


def submit_solution_part_1():
    submit_solution(part_1, 1)
    
    
def submit_solution_part_2():
    submit_solution(part_2, 1)


if __name__ == '__main__':
    input_content = pathlib.Path("input.txt").read_text()
    print(part_1(input_content))
    print(part_2(input_content))
    print(part_2(input_content) == 2752)
    # submit_solution_part_1()
    # submit_solution_part_2()
