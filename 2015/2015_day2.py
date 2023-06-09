# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from itertools import permutations
from functools import reduce
from operator import mul
from helpers.helper_functions import read_multiple_lines_to_list_of_str

def _split_to_ints(row: str) -> tuple[int]:
    """


    Parameters
    ----------
    row : str
        DESCRIPTION.

    Returns
    -------
    tuple[int]
        DESCRIPTION.

    """
    return tuple(int(num) for num in row.split("x"))

def part1(commands: str):
    """
    How many total square feet of wrapping paper should they order?

    Sum the area of all sides plus one times the smallest side.

    Parameters
    ----------
    commands : str
        The provides sides.

    Returns
    -------
    total_wrapping_needed : int
        Total square feet of wrapping paper needed.

    """
    total_wrapping_needed = 0
    for command in commands:
        length, width, height = _split_to_ints(command)
        sides = tuple(map(lambda x:x[0]*x[1],
                          permutations([length, width, height], 2)))
        wrapping_needed = sum(sides) + min(sides)
        total_wrapping_needed += wrapping_needed
    return total_wrapping_needed

def part2(commands: str):
    """
    How many total feet of ribbon should they order?

    Sum twice shortest sides plus the cube of the sides.

    Parameters
    ----------
    commands : str
        The provides sides.

    Returns
    -------
    total_length_needed : int
        Total length of ribbon needed.

    """
    total_length_needed = 0
    for command in commands:
        length, width, height = _split_to_ints(command)
        shortest_sides = sorted([length, width, height])[:2]
        ribbon_length = 2*sum(shortest_sides) + reduce(mul,
                                                       (length, width, height))
        total_length_needed += ribbon_length
    return total_length_needed

if __name__ == "__main__":
    instructions = read_multiple_lines_to_list_of_str("input_2015_2.txt")
    print(part1(instructions))
    print(part2(instructions))
