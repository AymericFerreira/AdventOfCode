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
    for jmp_number in range(0, len(commandList)):
        newList = open('day8Files\input.txt', 'r').read().split('\n')

        if newList[jmp_number] != newList[jmp_number].replace('nop', 'jmp'):
            newList[jmp_number] = newList[jmp_number].replace('nop', 'jmp')
            line = 0
            eol = True
            lineList = []
            acc = 0

            while eol:
                if line >= len(newList):
                    print(f'JMP {acc} acc')
                    eol = False
                else:
                    command = newList[line]
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

    for nop_number in range(0, len(commandList)):
        newList = open('day8Files\input.txt', 'r').read().split('\n')

        if newList[nop_number] != newList[nop_number].replace('jmp', 'nop'):
            newList[nop_number] = newList[nop_number].replace('jmp', 'nop')
            line = 0
            eol = True
            lineList = []
            acc = 0

            while eol:
                if line >= len(newList):
                    print(f'NOP {acc} acc')
                    eol = False
                else:
                    command = newList[line]
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

part_one()
part_two()
