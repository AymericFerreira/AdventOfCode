import sys
import re

file = open('day8Files\input.txt', 'r')
content = file.read()
commandList = content.split('\n')

def part_one():
    line = 0
    eol = True
    lineList = []
    acc = 0

    while eol:
        command = commandList[line]
        instruction, number = command.split()

        if line in lineList:
            eol = False

        else:
            lineList.append(line)

            if instruction == 'jmp':
                line += int(number)
            elif instruction == 'acc':
                line += 1
                acc += int(number)
            else:
                line += 1

    print(acc)


def part_two():
    for commutation_number in range(len(commandList)):
        newList = open('day8Files\input.txt', 'r').read().split('\n')

        if newList[commutation_number] != newList[commutation_number].replace('nop', 'jmp') or \
                newList[commutation_number] != newList[commutation_number].replace('jmp', 'nop'):
            if newList[commutation_number] != newList[commutation_number].replace('nop', 'jmp'):
                newList[commutation_number] = newList[commutation_number].replace('nop', 'jmp')
            else:
                newList[commutation_number] = newList[commutation_number].replace('jmp', 'nop')
            line = 0
            eol = True
            lineList = []
            acc = 0

            while eol:
                if line >= len(newList):
                    print(f'Accuracy value : {acc}')
                    eol = False
                else:
                    if line in lineList:
                        eol = False

                    else:
                        lineList.append(line)

                        command = newList[line]
                        instruction, number = command.split()

                        if instruction == 'acc':
                            line += 1
                            acc += int(number)
                        elif instruction == 'jmp':
                            line += int(number)
                        else:
                            line += 1


part_one()
part_two()
