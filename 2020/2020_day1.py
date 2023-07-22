# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_list_of_ints

def part1(expenses: list[int]) -> int:
    """
    Find the two entries that sum to 2020; what do you get if you multiply them together?


    """
    for pos, expense in enumerate(expenses):
        for other in expenses[pos:]:
            if expense + other == 2020:
                break
        else:
            continue
        break
    return expense * other

def part2(expenses: list[int]) -> int:
    """
    In your expense report, what is the product of the three entries that sum to 2020?


    """
    for pos1, expense in enumerate(expenses):
        for pos2, other in enumerate(expenses[pos1:]):
            for another in expenses[pos2:]:
                if expense + other + another == 2020:
                    break
            else:
                continue
            break
        else:
            continue
        break
    return expense * other * another

if __name__ == "__main__":
    instructions = read_multiple_lines_to_list_of_ints("input_2020_1.txt")
    print(part1(instructions))
    print(part2(instructions))
