file = open("day9Files\\input.txt", "r")
content = file.read()
commandList = content.split('\n')

numberList = [int(number) for number in commandList]

gap = 25


def part_one():
    for number in range(gap+1, len(numberList)):
        listOfNumbers = numberList[number-gap:number]
        equality = False
        for number1 in listOfNumbers:
            for number2 in listOfNumbers:
                if numberList[number] == (number1 + number2):
                    equality = True
                    break
            if equality:
                break
        if not equality:
            print(f"{numberList[number]} failed to pass ")
            return numberList[number]


def part_two():
    number = part_one()
    numberSumList = []
    for i in range(len(numberList)):
        print(f"i : {i}")
        for j in range(i, len(numberList)):
            sumOfNumbers = 0
            numberSumList.append(numberList[j])
            while sumOfNumbers < number:
                sumOfNumbers += numberList[j]
            if sumOfNumbers == number and len(numberSumList) > 2:
                print(numberSumList, number)
                print(max(numberSumList) + min(numberSumList))
            else:
                numberSumList = []


    # pass

# part_one()
part_two()