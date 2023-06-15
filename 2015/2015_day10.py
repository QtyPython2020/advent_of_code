# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_str

def _look_say(number: str):
    """
    Apply the Look-and-Say rules to the string of digits.

    Parameters
    ----------
    number : str
        The input number.

    Returns
    -------
    sets : str
        The output number.

    """
    if len(number) == 1:
        return f"1{number}"
    value = number[0]
    count = 1
    sets = ""
    for num in number[1:]:
        if num == value:
            count += 1
        elif num != value:
            sets += f"{count}{value}"
            value = num
            count = 1
    sets += f"{count}{value}"
    return sets


def part1(digits: str):
    """
    What is the length of the result?

    Parameters
    ----------
    digits : str
        The starting number.

    Returns
    -------
    int
        The length of the result.

    """
    for _ in range(40):
        digits = _look_say(digits)
    return len(digits)


def part2(digits: str):
    """
    What is the length of the new result?

    Parameters
    ----------
    digits : str
        The starting number.

    Returns
    -------
    int
        The length of the result.

    """
    for _ in range(50):
        digits = _look_say(digits)
    return len(digits)

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2015_10.txt")
    print(part1(instructions))
    print(part2(instructions))
