# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_list_of_ints

def part1(commands: str):
    """
    How many steps does it take to reach the exit?
    """
    steps = 0
    position = 0
    commands = list(commands)
    while True:
        # get offset
        offset = commands[position]
        # increment instruction
        commands[position] += 1
        # get new position
        position += offset
        # increment steps
        steps += 1
        if position < 0 or position >= len(commands):
            break
    return steps

def part2(commands: str):
    """
    How many steps does it now take to reach the exit?
    """
    steps = 0
    position = 0
    commands = list(commands)
    while True:
        # get offset
        offset = commands[position]
        # increment instruction
        commands[position] = offset + 1 if offset < 3 else offset - 1
        # get new position
        position += offset
        # increment steps
        steps += 1
        if position < 0 or position >= len(commands):
            break
    return steps

if __name__ == "__main__":
    instructions = read_multiple_lines_to_list_of_ints("input_2017_5.txt")
    print(part1(instructions))
    print(part2(instructions))
