# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from collections import Counter
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    """
    What is the error-corrected version of the message being sent?
    """
    word = ""
    for index in range(len(commands[0])):
        letter = Counter(command[index] for command in commands).most_common(1)[0][0]
        word += letter
    return word

def part2(commands: str):
    """
    Given the recording in your puzzle input and this new decoding methodology,
    what is the original message that Santa is trying to send?
    """
    word = ""
    for index in range(len(commands[0])):
        letter = sorted(Counter(command[index] for command in commands).items(),
                        key=lambda x:x[1])[0][0]
        word += letter
    return word

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2016_6.txt")
    print(part1(instructions))
    print(part2(instructions))
