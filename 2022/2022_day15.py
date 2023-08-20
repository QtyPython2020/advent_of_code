# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    grid = [["." for _ in range(10**6)] for _ in range(10**6)]
    # for command in commands:
    #     coords = re.findall("x=(-?\d*),\sy=(-?\d*)", command)
    #     sx, sy = list(map(int,coords[0]))
    #     bx, by = list(map(int,coords[1]))
    #     grid[sy+500000][sx+2] = "s"
    #     grid[by+500000][bx+2] = "b"

    #     break
    for row in grid:
        print("".join(row))

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_15.txt")
    print(part1(instructions))
    print(part2(instructions))
