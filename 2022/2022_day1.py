# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: tuple):
    """
    Find the Elf carrying the most Calories.
    How many total Calories is that Elf carrying?

    Parameters
    ----------
    commands : tuple
        The calories carried by the elfs.

    Returns
    -------
    highest_count : int
        The highest sum of calories carried by one elf.

    """
    highest_count, count = 0, 0
    for command in commands:
        if command == "":
            highest_count = max(highest_count, count)
            count = 0
            continue
        count += int(command)
    return highest_count

def part2(commands: tuple):
    """
    Find the top three Elves carrying the most Calories.
    How many Calories are those Elves carrying in total?

    Parameters
    ----------
    commands : tuple
        The calories carried by the elfs.

    Returns
    -------
    sum_top_three : int
        The sum of the top three elves carrying calories.

    """
    loads_per_elf = set()
    count = 0
    for command in commands:
        if command == "":
            loads_per_elf.add(count)
            count = 0
            continue
        count += int(command)
    sum_top_three = sum(sorted(loads_per_elf, reverse=True)[:3])
    return sum_top_three

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_1.txt")
    print(part1(instructions))
    print(part2(instructions))
