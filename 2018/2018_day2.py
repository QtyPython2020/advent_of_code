# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from collections import Counter
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str



def part1(commands: str):
    """

    """
    doubles = 0
    triples = 0
    for command in commands:
        letter_counts = set(Counter(command).values())
        if 2 in letter_counts:
            doubles += 1
        if 3 in letter_counts:
            triples += 1
    checksum = doubles * triples
    return checksum

def part2(commands: str):
    """

    """
    for index, command in enumerate(commands):
        letters = set(sorted(command))
        for box_id in commands[index+1:]:
            other_letters = set(sorted(box_id))
            if len(letters.difference(other_letters)) == 1 and\
                sum(l!=o for l,o in zip(letters,other_letters)) == 1:
                    return "".join(l for l,o in zip(command, box_id) if l==o)

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_2.txt")
    print(part1(instructions))
    print(part2(instructions))
