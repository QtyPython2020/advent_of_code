# -*- coding: utf-8 -*-
"""
@author: QtyPython2020
"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def part1(commands: str) -> int:
    """
    How many passphrases are valid?
    Use the length of the set of words to check if all words are unique.
    """
    valid_passphrases = sum(len(command)==len(set(command))
                            for command in commands)
    return valid_passphrases

def part2(commands: str):
    """
    How many passphrases are valid?
    Use the length of the set of words to check if all words are unique after having
    sorted all the letters in the individual words.
    """
    valid_passphrases =  sum(len(command)==len(set("".join(sorted(el))
                                                   for el in command))
                             for command in commands)
    return valid_passphrases

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2017_4.txt",
                                                                  "str")
    print(part1(instructions))
    print(part2(instructions))
