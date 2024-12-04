import re
import numpy as np
from aoc_template import submit, prepare_day, read_file_to_str
from benchmarking import FunctionBenchmark
import time
from typing import List, Tuple, Union


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        if len(self.queue) == 0:
            self.queue.append(item)
            return self
        if self.queue[-1] == "don't()" and item != "do()":
            pass
        elif self.queue[-1] == "don't()":
            self.queue.pop()
        else:
            self.queue.append(item)

        return self

    def process_queue(self):
        for queue in self.queue:
            if queue in ["don't()", "do()"]:
                self.queue.remove(queue)
        return sum(
            map(lambda x: int(x[0]) * int(x[1]) if len(x) == 2 else 0, self.queue)
        )


def parse_instructions(content: str) -> List[Union[str, Tuple[str, str]]]:
    simple_pattern = r"don't\(\)|do\(\)"
    mul_pattern = r"mul\((\d+),(\d+)\)"

    simple_matches = re.finditer(simple_pattern, content)
    instructions = [(match.start(), match.group()) for match in simple_matches]

    mul_matches = re.finditer(mul_pattern, content)
    for match in mul_matches:
        instructions.append((match.start(), (match.group(1), match.group(2))))

    return [instruction[1] for instruction in sorted(instructions)]


def part_1(content: str) -> int:
    matches = re.findall(r"mul\((\d+),(\d+)\)", content)
    return sum(map(lambda x: int(x[0]) * int(x[1]), matches))


def part_2(content: str) -> int:
    queue = Queue()
    instruction_match = parse_instructions(content)
    for match in instruction_match:
        queue.push(match)
    return queue.process_queue()


example = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


if __name__ == "__main__":
    # example, input = prepare_day(__file__)
    print(part_1(example))
    # submit(2024, 3, part_1(read_file_to_str(__file__)))
    # print(part_2(example))
    print(part_2(read_file_to_str(__file__)))
