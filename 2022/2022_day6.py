# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_str

def part1(strng: str):
    """
    How many characters need to be processed before the first start-of-packet marker is detected?

    Cycle through the strings to find if there are four unique letters and return the index of the
    next letter.
    """
    for i in range(4, len(strng)+1):
        unique = len(set(strng[i-4:i]))
        if unique == 4:
            break
        continue
    return i

def part2(strng: str):
    """
    How many characters need to be processed before the first start-of-message marker is detected?

    Cycle through the strings to find if there are fourteen unique letters and return the index of
    the next letter.
    """
    for i in range(14, len(strng)+1):
        unique = len(set(strng[i-14:i]))
        if unique == 14:
            break
        continue
    return i

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2022_6.txt")
    print(part1(instructions))
    print(part2(instructions))
