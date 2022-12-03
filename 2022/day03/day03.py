import pathlib
from utils.post_answer import submit_solution


def part_1(input: str):
    lines = input.splitlines()
    priority = 0
    for line in lines:
        compartment1 = set(line[:len(line)//2])
        compartment2 = set(line[len(line)//2:])
        letter = compartment1.intersection(compartment2)
        if list(letter)[0].isupper():
            priority += ord(list(letter)[0]) - 64 + 26
        else:
            priority += ord(list(letter)[0]) - 96
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
    for elf1, elf2, elf3, elf4, elf5, elf6 in \
            zip(lines[::6], lines[1::6], lines[2::6], lines[3::6], lines[4::6], lines[5::6]):
        compartiment1 = set(elf1).intersection(set(elf2)).intersection(set(elf3))
        compartiment2 = set(elf4).intersection(set(elf5)).intersection(set(elf6))
        priority += convert_to_priority(compartiment1)
        priority += convert_to_priority(compartiment2)
    return priority



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
