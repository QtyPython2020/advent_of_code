# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_list_of_ints

def part1(measurements: str):
    """
    How many measurements are larger than the previous measurement?

    Go through the measurements and compare each with the last measures and add one
    to the count for each time the measure is larger than the previous.
    """
    increases = 0
    last = None

    for measure in measurements:
        if last is None:
            last = measure
            continue
        increases += (measure > last)
        last = measure
    return increases

def part2(measurements: str):
    """
    How many sums are larger than the previous sum?

    Going through the measures add one count if the sum of three consecutive measurements
    is larger than the sum of the three before that.
    """
    increases = 0

    for index, _ in enumerate(measurements[3:], 3):
        increases += sum(measurements[index-3: index]) < sum(measurements[index-2: index+1])
    return increases

if __name__ == "__main__":
    instructions = read_multiple_lines_to_list_of_ints("input_2021_1.txt")
    print(part1(instructions))
    print(part2(instructions))
