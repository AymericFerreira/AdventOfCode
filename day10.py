file = open("day10Files/input.txt", "r")
content = file.read()
commandList = content.split('\n')

numberList = [int(number) for number in commandList]
numberList.append(0)
numberList.append(max(numberList) +3)

gap = 25


def part_one():
    numbers_sorted = sorted(numberList)
    oneJolt = 0
    threeJolt = 0
    for i in range(len(numberList) - 1):
        if numbers_sorted[i+1] == numbers_sorted[i] + 1:
            oneJolt += 1
        elif numbers_sorted[i+1] == numbers_sorted[i] + 3:
            threeJolt += 1
    print(oneJolt * threeJolt)



# def part_two():
#     number = part_one()
#     numberSumList = []
#     for i in range(len(numberList)):
#         print(f"i : {i}")
#         for j in range(i, len(numberList)):
#             sumOfNumbers = 0
#             numberSumList.append(numberList[j])
#             while sumOfNumbers < number:
#                 sumOfNumbers += numberList[j]
#             if sumOfNumbers == number and len(numberSumList) > 2:
#                 print(numberSumList, number)
#                 print(max(numberSumList) + min(numberSumList))
#             else:
#                 numberSumList = []
#
#
#     # pass

part_one()
# part_two()