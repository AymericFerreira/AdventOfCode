file = open('day2Files\input.txt', 'r')
content = file.read()
commandList = content.split()


def parser(line):
    line = line.split(' ')
    numbers = line[0].split('-')
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    letter = line[1][0]
    password = line[2]
    return test_condition(number1, number2, password, letter)


def parser2(line):
    line = line.split(' ')
    numbers = line[0].split('-')
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    letter = line[1][0]
    password = line[2]
    return test_condition2(number1, number2, password, letter)


def test_condition(number1, number2, password, letter):  # sourcery skip: sum-comprehension
    count = 0
    for passwordLetter in password:
        if letter == passwordLetter:
            count += 1

    if count >= number1 and count <= number2:
        return True


def test_condition2(number1, number2, password, letter):
    if password[number1-1] == letter and password[number2-1] != letter:
        return True
    if password[number1 - 1] != letter and password[number2 - 1] == letter:
        return True


def first_condition():  # sourcery skip: sum-comprehension
    passWordValidated = 0
    for line in commandList:
        if parser(line):
            passWordValidated += 1
    print(passWordValidated)


def second_condition():
    passWordValidated = 0  # sourcery skip: sum-comprehension
    for line in commandList:
        if parser2(line):
            passWordValidated += 1
    print(passWordValidated)


if __name__ == '__main__':
    # first_condition()
    second_condition()
