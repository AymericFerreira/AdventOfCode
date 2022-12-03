import pathlib
from utils.post_answer import submit_solution


def part_1(input: str):
    correspondance = {"A X": 4, "A Y": 8, "A Z": 3,
                      "B X": 1, "B Y": 5, "B Z": 9,
                      "C X": 7, "C Y": 2, "C Z": 6}
    combinations = input.splitlines()
    score = 0
    for combination in combinations:
        score += correspondance[combination]
    return score


def part_2(input: str):
    correspondance = {"A X": 3, "A Y": 4, "A Z": 8,
                      "B X": 1, "B Y": 5, "B Z": 9,
                      "C X": 2, "C Y": 6, "C Z": 7}
    combinations = input.splitlines()
    score = 0
    for combination in combinations:
        score += correspondance[combination]
    return score


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
