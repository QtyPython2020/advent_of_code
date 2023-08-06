# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import numpy as np
from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def _get_neighbours(floor: tuple[tuple[int]],
                    point: tuple[int]) -> tuple[tuple[int]]:
    pos_x, pos_y = point
    return tuple([np.inf if pos_y==0 else floor[pos_y-1][pos_x], #top
                  np.inf if pos_y+1==len(floor) else floor[pos_y+1][pos_x], #bottom
                  np.inf if pos_x==0 else floor[pos_y][pos_x-1], #left
                  np.inf if pos_x+1==len(floor[pos_y]) else floor[pos_y][pos_x+1] #right
                  ]
                 )

def part1(grid: tuple[tuple[int]]):
    """
    What is the sum of the risk levels of all low points on your heightmap?
    """
    risk_level = []
    for pos_y, row in enumerate(grid):
        for pos_x, cell in enumerate(row):
            neighbours = _get_neighbours(grid, (pos_x, pos_y))
            if cell < min(neighbours):
                risk_level.append(cell+1)
    risk_levels = sum(risk_level)
    return risk_levels

def part2(grid: tuple[tuple[int]]):
    """
    What do you get if you multiply together the sizes of the three largest basins?
    """
    bassins = []
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2021_9_test.txt",
                                                                  "ints")
    print(part1(instructions))
    print(part2(instructions))
