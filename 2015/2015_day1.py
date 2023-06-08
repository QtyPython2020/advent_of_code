# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_str

def part1(commands: str) -> int:
    """
    To what floor do the instructions take Santa?

    Take all directions and sum up all the upwards directions and subtract the
    downward directions. The result is the final floor.

    Parameters
    ----------
    commands : str
        The provided directions.

    Returns
    -------
    final_floor : int
        The final floor on which Santa lands.

    """
    upward = commands.count("(")
    downward = commands.count(")")
    final_floor = upward - downward
    return final_floor

def part2(commands: str) -> int:
    """
    What is the position of the character that causes Santa to first enter the basement?

    Go through all the directions until the floor becomes -1.

    Parameters
    ----------
    commands : str
        The provided directions.

    Returns
    -------
    int
        The position of the direction that lets Santa enter the basement.

    """
    floor = 0
    for position, command in enumerate(commands, 1):
        floor += 1 if command == "(" else -1
        # stop when Santa enters the basement
        if floor == -1:
            return position
    return None

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2015_1.txt")
    print(part1(instructions))
    print(part2(instructions))
