# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from helpers.helper_functions import read_single_line_to_list_of_int

def part1(number_range: list[int]):
    """
    How many different passwords within the range given in your puzzle input meet
    these criteria?

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same .
    Going from left to right, the digits never decrease; they only ever increase
    or stay the same.

    The numbers are always within the range and a six-digit number so the check is
    only done on the other criteria
    """
    count = 0
    for number in range(*number_range):
        ints = list(map(int, str(number)))
        doubles = 0
        for pos, int_ in enumerate(ints[1:], 1):
            # decreasing range
            if int_ < ints[pos-1]:
                break
            # adjacent values
            if int_ == ints[pos-1]:
                doubles += 1
        else:
            if doubles:
                count += 1
    return count


def part2(number_range: list[int]):
    """
    How many different passwords within the range given in your puzzle input meet
    all of the criteria?

    The two adjacent matching digits are not part of a larger group of matching digits.
    """
    count = 0
    for number in range(*number_range):
        ints = list(map(int, str(number)))
        doubles = set()
        multiples = set()
        for pos, int_ in enumerate(ints[1:], 1):
            # decreasing range
            if int_ < ints[pos-1]:
                break
            # adjacent values
            if int_ == ints[pos-1]:
                doubles.add(int_)
                if pos < 5 and int_ == ints[pos+1]:
                    multiples.add(int_)
        else:
            if doubles.difference(multiples):
                count += 1
    return count

if __name__ == "__main__":
    instructions = read_single_line_to_list_of_int("input_2019_4.txt", "-")
    print(part1(instructions))
    print(part2(instructions))
