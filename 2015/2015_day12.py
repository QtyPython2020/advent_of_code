# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_json_to_object

def _count_numbers(json_part, count=0):
    """

    """
    if isinstance(json_part, dict):
        json_part = json_part.values()
    for element in json_part:
        if isinstance(element, (dict, list)):
            count = _count_numbers(element, count)
        elif isinstance(element, str):
            count += 0
        else:
            count += element
    return count

def _count_non_red_numbers(json_part, count=0):
    """

    """
    if isinstance(json_part, dict):
        if "red" in json_part.values():
            return count
        json_part = json_part.values()
    for element in json_part:
        if isinstance(element, (dict, list)):
            count = _count_non_red_numbers(element, count)
        elif isinstance(element, str):
            count += 0
        else:
            count += element
    return count

def part1(commands: str):
    return _count_numbers(commands)

def part2(commands: str):
    return _count_non_red_numbers(commands)

if __name__ == "__main__":
    instructions = read_json_to_object("input_2015_12.txt")
    print(part1(instructions))
    print(part2(instructions))
