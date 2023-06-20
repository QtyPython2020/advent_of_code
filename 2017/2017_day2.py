# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def part1(spreadsheet: str):
    """
    What is the checksum for the spreadsheet in your puzzle input?
    """
    checksum = sum(max(row) - min(row) for row in spreadsheet)
    return checksum

def part2(spreadsheet: str):
    """
    What is the sum of each row's result in your puzzle input?
    """
    checksum = 0
    for row in spreadsheet:
        numbers = sorted(row)[::-1]
        for num in numbers:
            for other in numbers[numbers.index(num)+1:]:
                if num/other == num//other:
                    checksum += num//other
                    break
                continue
            else:
                continue
    return checksum

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2017_2.txt",
                                                                  "int")
    print(part1(instructions))
    print(part2(instructions))
