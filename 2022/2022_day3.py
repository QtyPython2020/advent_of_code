# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    """
    What is the sum of the priorities of those item types?

    To define the priorities for each item divide in two equal parts, look for the
    common letter and add the letter value based on the ASCII value of the letter.
    """
    priorities = 0
    for command in commands:
        length = len(command)
        left, right = set(command[:length//2]), set(command[length//2:])
        overlap = set(letter for letter in left).intersection(set(letter for letter in right))
        priorities += [ord(o)-96 if o.islower() else ord(o)-38 for o in overlap][0]
    return priorities

def part2(commands: str):
    """
    What is the sum of the priorities of those item types?

    To define the priorities for each item divide in two equal parts, look for the
    common letter and add the letter value based on the ASCII value of the letter.
    """
    priorities = 0
    for index in range(0, len(commands), 3):
        one, two, three =  set(letter for letter in commands[index]),\
            set(letter for letter in commands[index+1]),\
                set(commands[index+2])
        overlap = one.intersection(two.intersection(three))
        priorities += [ord(o)-96 if o.islower() else ord(o)-38 for o in overlap][0]
    return priorities

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_3.txt")
    print(part1(instructions))
    print(part2(instructions))
