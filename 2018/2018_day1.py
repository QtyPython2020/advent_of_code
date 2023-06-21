# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_list_of_ints

def part1(changes: list[int]) -> int:
    """

    """
    frequency = sum(changes)
    return frequency

def part2(changes: list[int]) -> int:
    """

    """
    pass

if __name__ == "__main__":
    instructions = read_multiple_lines_to_list_of_ints("input_2018_1.txt")
    print(part1(instructions))
    print(part2([-6, +3, +8, +5, -6]))
