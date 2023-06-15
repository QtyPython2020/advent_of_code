# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import ast
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _encode(literal: str):
    """
    Create a new string literal with the new encoding rules.

    Parameters
    ----------
    literal : str
        DESCRIPTION.

    Returns
    -------
    new_string : TYPE
        DESCRIPTION.

    """
    new_string = "".join(letter if letter.isalnum() else f"\\{letter}" for letter in literal)
    return new_string + "''"

def part1(commands: tuple[str]):
    """
    What is the number of characters of code for string literals minus the number
    of characters in memory for the values of the strings in total for the entire file?

    Parameters
    ----------
    commands : tuple[str]
        All the literal strings.

    Returns
    -------
    total_number_of_characters : int
        The sum of the number of characters.

    """
    total_number_of_characters = sum(len(command) - len(ast.literal_eval(command))
                                     for command in commands)
    return total_number_of_characters

def part2(commands: tuple[str]):
    """
    What is the total number of characters to represent the newly encoded strings
    minus the number of characters of code in each original string literal?

    Parameters
    ----------
    commands : tuple[str]
        All the literal strings.

    Returns
    -------
    total_number_of_characters : int
        The sum of the number of characters.

    """
    total_number_of_characters = sum(len(_encode(command)) - len(command)
                                     for command in commands)
    return total_number_of_characters

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2015_8.txt")
    print(part1(instructions))
    print(part2(instructions))
