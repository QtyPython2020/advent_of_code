# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _parse_records(record: str):
    """

    """
    date, time, action = re.findall(r"\[1518-(\d{1,2}-\d{1,2})\s(\d{2}:\d{2})\]\s(.*)",
                                    record)[0]
    return date, time, action

def part1(commands: str):
    for command in commands:
        print(_parse_records(command))

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_4.txt")
    print(part1(instructions))
    print(part2(instructions))
