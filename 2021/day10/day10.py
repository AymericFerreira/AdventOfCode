import pathlib
from utils.post_answer import submit_solution


class QueueList:
    def __init__(self):
        self.queue = []
        self.queue_length = -1
        self.correspondence = correspondence_dict()

    def add(self, element):
        self.queue.append(element)
        self.queue_length += 1
        return self

    def popd(self):
        self.queue.pop(self.queue_length)
        self.queue_length -= 1
        return self

    def look(self):
        if self.queue_length == -1:
            return None
        return self.queue[self.queue_length]

    def check(self, element):
        if element in self.correspondence.values():
            self.add(element)
            return None
        if self.look() == self.correspondence.get(element):
            self.popd()
            return None
        else:
            return element


def correspondence_dict():
    return {")": "(",
            "]": "[",
            "}": "{",
            ">": "<"}


def reversed_correspondence_dict():
    return {v: k for k, v in correspondence_dict().items()}


def score_dict():
    return {")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137}


def score_dict_part2():
    return {")": 1,
            "]": 2,
            "}": 3,
            ">": 4}


def get_score(element, illegal_score_dict):
    if element is None:
        return 0
    return illegal_score_dict.get(element)


def part_1(input: str):
    illegal_score_dict = score_dict()
    score = 0
    for line in input.splitlines():
        q = QueueList()

        for element in line:
            temp_score = get_score(q.check(element), illegal_score_dict)
            score += temp_score
            if temp_score > 0:
                break
    return score


def part_2(input: str):
    illegal_score_dict = score_dict()
    score = []
    for line in input.splitlines():
        q = QueueList()
        for i, element in enumerate(line):
            temp_score = get_score(q.check(element), illegal_score_dict)
            if temp_score > 0:
                break
            if i == len(line) - 1:
                score.append(compute_score_of_incomplete_line(q.queue))

    return sorted(score)[len(score) // 2]


def compute_score_of_incomplete_line(queue: [str]):
    score = 0
    for element in queue[::-1]:
        score = get_score_part2(reversed_correspondence_dict().get(element), score)
    return score


def get_score_part2(element, score: int = 0):
    return score * 5 + score_dict_part2().get(element)


def submit_solution_part_1():
    submit_solution(part_1, 1)


def submit_solution_part_2():
    submit_solution(part_2, 1)


if __name__ == '__main__':
    input_content = pathlib.Path("input.txt").read_text()
    a = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    print(part_1(input_content))
    # print(part_2(a))
    print(part_2(input_content))
    # submit_solution_part_1()
    # submit_solution_part_2()
