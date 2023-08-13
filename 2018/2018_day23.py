# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _make_nanobots(lines: tuple[str]):
    """

    """
    list_bots =[]
    for line in lines:
        *pos, radius = list(map(int, re.findall(r"(\d+)", line)
                                )
                            )
        list_bots.append([pos, radius])
    return list_bots

def part1(commands: str):
    in_range = 0
    nano_bots = _make_nanobots(commands)
    strongest = max(nano_bots, key=lambda x:x[-1])
    center_position, max_range = strongest
    for bot in nano_bots:
        pos, _ = bot
        range_ = sum(map(lambda positions:abs(positions[0]-positions[1]),
                         zip(center_position, pos)
                         )
                     )
        print(range_)
        in_range += max_range >= range_
    return in_range

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_23.txt")
    print(part1(instructions))
    print(part2(instructions))
