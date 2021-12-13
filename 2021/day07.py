import re
import numpy as np


def input_to_list_int(input_content: str) -> list[int]:
    return list(map(int, re.findall("\d+", input_content)))


def calculate_minimum_fuel(input_content):
    numberList = input_to_list_int(input_content)
    return sum(np.absolute(numberList - np.median(numberList)))


def calculate_ponderate_minimum_fuel(input_content):
    numberList = input_to_list_int(input_content)
    fuelCost = np.array(numberList) - np.mean(numberList) // 1
    totalFuelCost = 0
    for fuel in fuelCost:
        fuel = abs(fuel)
        totalFuelCost += np.round((fuel * fuel + fuel) / 2)
    print(totalFuelCost)

if __name__ == '__main__':
    with open("day07/input.txt") as input_file:
        input_content = input_file.read()
    # print(calculate_minimum_fuel(input_content))
    calculate_ponderate_minimum_fuel(input_content)
