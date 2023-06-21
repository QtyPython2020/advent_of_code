# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _parse_claims(line: str) -> tuple[str, int, int, int, int]:
    """

     """
    claim_id, *others = re.findall(r"#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)",
                                   line)[0]
    pos_x, pos_y, width, height = (int(num) for num in others)
    return claim_id, pos_x, pos_y, width, height

def part1(claims: tuple[str]):
    grid = [[0*1000] * 1000]
    # for claim in claims:
    #     _, offset_x, offset_y, width, height = _parse_claims(claim)
    #     pos_x, pos_y = offset_x, offset_y
    #     for h in range(height):
    #         for w in range(width):
    #             print(pos_y)
    #             grid[pos_y][pos_x] += 1
    #             pos_x += 1
    #             pos_y += 1
    return grid

def part2(claims: tuple[str]):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_3.txt")
    print(part1(x:=instructions))
    print(part2(instructions))
