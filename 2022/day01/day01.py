import pathlib
from utils.post_answer import submit_solution


class Elf:
    def __init__(self):
        self.calories = []

    def add_calorie(self, calorie: int):
        self.calories.append(calorie)

    def get_total_calories(self):
        return sum(self.calories)


def part_1(input: str):
    calories = input.splitlines()
    elf_list = [Elf()]
    for calorie in calories:
        if calorie != "":
            elf_list[-1].add_calorie(int(calorie))
        else:
            elf_list.append(Elf())
    highest_calories_idx = 0
    for elf in elf_list:
        if elf.get_total_calories() > elf_list[highest_calories_idx].get_total_calories():
            highest_calories_idx = elf_list.index(elf)
    return elf_list[highest_calories_idx].get_total_calories()


def part_2(input: str):
    calories = input.splitlines()
    elf_list = [Elf()]
    for calorie in calories:
        if calorie != "":
            elf_list[-1].add_calorie(int(calorie))
        else:
            elf_list.append(Elf())
    calorie_list = []
    for elf in elf_list:
        calorie_list.append(elf.get_total_calories())
    return sum(sorted(calorie_list, reverse=True)[:3])


def submit_solution_part_1():
    submit_solution(part_1, 1)
    
    
def submit_solution_part_2():
    submit_solution(part_2, 1)


if __name__ == '__main__':
    input_content = pathlib.Path("input.txt").read_text()
    # print(input_content.splitlines())
    # print(part_1(input_content))
    # submit_solution_part_1()
    print(part_2(input_content))
    # submit_solution_part_1()
    # submit_solution_part_2()
