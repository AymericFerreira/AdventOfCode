from math import factorial

file = open("day10Files/input.txt", "r")
content = file.read()
commandList = content.split('\n')

numberList = [int(number) for number in commandList]
numberList.append(0)  # first condition
numberList.append(max(numberList) + 3)  # last condition


def part_one():
    numbers_sorted = sorted(numberList)
    oneJolt = 0
    threeJolt = 0
    for i in range(len(numberList) - 1):
        if numbers_sorted[i + 1] == numbers_sorted[i] + 1:
            oneJolt += 1
        elif numbers_sorted[i + 1] == numbers_sorted[i] + 3:
            threeJolt += 1
    print(oneJolt * threeJolt)


def count_combination(numberList):
    if len(numberList) <= 2:
        return 1
    elif len(numberList) == 3:
        return 2
    else:
        return 1 + len(numberList) - 2 + int(factorial(len(numberList) - 2) / 2)


def part_two():
    numbers_sorted = sorted(numberList)
    result = 1
    begin = 0
    end = 0
    while begin < len(numbers_sorted) - 1 and end < len(numbers_sorted) - 1:
        while numbers_sorted[end + 1] - numbers_sorted[end] == 1:
            end += 1
        result *= count_combination(numbers_sorted[begin:end + 1])
        end += 1
        begin = end
    print(result)


part_one()
part_two()
