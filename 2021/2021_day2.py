# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    """
    What do you get if you multiply your final horizontal position by your final depth?

    While following the commands adjust horizontal position and depth accordingly.
    """
    horizon, depth = 0, 0
    for command in commands:
        if command.startswith("forward"):
            horizon += int(command[-1])
        elif command.startswith("down"):
            depth += int(command[-1])
        elif command.startswith("up"):
            depth -= int(command[-1])
    return horizon * depth

def part2(commands: str):
    """
    What do you get if you multiply your final horizontal position by your final depth?

    While following the commands adjust aim, and horizontal position and depth accordingly.
    """
    horizon, depth, aim = 0, 0, 0
    for command in commands:
        if command.startswith("forward"):
            horizon += int(command[-1])
            depth += aim * int(command[-1])
        elif command.startswith("down"):
            aim += int(command[-1])
        elif command.startswith("up"):
            aim -= int(command[-1])
    return horizon * depth

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2021_2.txt")
    print(part1(instructions))
    print(part2(instructions))
