# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    """
    How many passwords are valid according to their policies?
    """
    valids = 0
    for command in commands:
        begin, end, letter, password = re.findall(r"(\d*)\-(\d*)\s(\w):\s(.*)", command)[0]
        if int(begin) <= password.count(letter) <= int(end):
            valids += 1
    return valids

def part2(commands: str):
    """
    How many passwords are valid according to the new interpretation of the policies?
    """
    valids = 0
    for command in commands:
        begin, end, letter, password = re.findall(r"(\d*)\-(\d*)\s(\w):\s(.*)", command)[0]
        if sum([password[int(begin)-1] == letter, password[int(end)-1] == letter]) == 1:
            valids += 1
    return valids

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2020_2.txt")
    print(part1(instructions))
    print(part2(instructions))
