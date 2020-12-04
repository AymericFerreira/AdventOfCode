file = open('day1Files\input.txt', 'r')
content = file.read()
numberList = content.split()


def two_numbers():
    for number1 in numberList:
        for number2 in numberList:
            if int(number1) + int(number2) == 2020:
                print(f"Number found {number1}, {number2} : {int(number1) * int(number2)}")
                exit()


def three_numbers():
    for number1 in numberList:
        for number2 in numberList:
            for number3 in numberList:
                if int(number1) + int(number2) + int(number3) == 2020:
                    print(f"Number found {number1}, {number2}, {number3} : {int(number1) * int(number2) * int(number3)}")
                    exit()


if __name__ == '__main__':
    three_numbers()
