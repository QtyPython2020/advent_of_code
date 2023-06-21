# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _find_abba(seq: str):
    for index in range(3, len(seq)):
        if seq[index-3] == seq[index] and seq[index-2] == seq[index-1]:
            return True
    return False

def part1(commands: str):
    tls_supporting_ips = 0
    for command in commands:
        first_part, bracket, second_part = re.findall(r"(\w*)\[(\w*)\](\w*)", command)[0]
        if _find_abba(bracket):
            continue
        if _find_abba(first_part) or _find_abba(second_part):
            tls_supporting_ips += 1
    return tls_supporting_ips

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2016_7.txt")
    print(part1(instructions))
    print(part2(instructions))
