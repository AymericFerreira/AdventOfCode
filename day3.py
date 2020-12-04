file = open('day3Files\input.txt', 'r')
content = file.read()
commandList = content.split()


def extend_data(commandList):
    # multiplicator = int(len(commandList)/3/len(commandList[0]))+1
    multiplicator = int(7*len(commandList)/len(commandList[0]))+1
    return [pattern * multiplicator for pattern in commandList]


def slope_traveller(commandList, right=3, down=1):
    xPos = 0
    numberOfTree = 0
    newData = extend_data(commandList)
    i = 0
    while i < len(newData):
        if newData[i][xPos] == "#":
            numberOfTree += 1
        xPos += right
        i += down
    return numberOfTree

finalNumber = 1
for right, down in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    finalNumber = finalNumber * slope_traveller(commandList, right, down)

print(finalNumber)
#
# xPos = 0
# numberOfTree = 0
# for line in extend_data(commandList):
#     if line[xPos] == "#":
#         numberOfTree +=1
#     xPos += 3
#
# print(numberOfTree)