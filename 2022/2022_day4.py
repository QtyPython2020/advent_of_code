# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def part1(commands: str):
    """
    In how many assignment pairs does one range fully contain the other?

    Determine the overlap by making sets of the ranges and checking whether one range
    is fully contained in the other.
    """
    doubles = 0
    for command in commands:
        range_one = set(range(command[0], command[1]+1))
        range_two = set(range(command[2], command[3]+1))
        overlap = range_one.issubset(range_two) + range_one.issuperset(range_two)
        if overlap:
            doubles += 1
    return doubles

def part2(commands: str):
    """
    In how many assignment pairs do the ranges overlap?

    Determine the overlap by making sets of the ranges and checking whether one range
    overlaps the other.
    """
    doubles = 0
    for command in commands:
        range_one = set(range(command[0], command[1]+1))
        range_two = set(range(command[2], command[3]+1))
        overlap = range_one.intersection(range_two)
        if overlap:
            doubles += 1
    return doubles

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2022_4.txt",
                                                                  "int")
    print(part1(instructions))
    print(part2(instructions))
