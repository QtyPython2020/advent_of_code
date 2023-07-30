# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _make_grid(size: int)-> list[list[int]]:
    """
    Make a square grid of zeroes with the given sides.
    """
    grid = [[0 for _ in range(size)] for _ in range(size)]
    return grid

def _extract_start_end(line: str) -> tuple[int]:
    """
    Extract all numeric values from the line and return a tuple of converted numbers.
    """
    positions = re.findall(r"\d+", line)
    return tuple(int(pos) for pos in positions)

def _describe_vent(start_x, start_y, end_x, end_y):
    """
    Describe all the points of a vent by first finding the length difference, then
    determine the direction of the vent and lastly generate all the points.
    """
    diff_x = end_x - start_x
    diff_y = end_y - start_y
    diff = max(abs(diff_x), abs(diff_y))
    dir_x = 0 if diff_x == 0 else diff_x//diff
    dir_y = 0 if diff_y == 0 else diff_y//diff
    vent = [(start_x+incr*dir_x,start_y+incr*dir_y)
            for incr in range(diff+1)]
    return vent

def _update_ocean_floor(grid: list[list[int]],
                        vent_parts: list[int]) -> list[list[int]]:
    """
    For every point of a vent update the grid.
    """
    for part in vent_parts:
        pos_x, pos_y = part
        grid[pos_y][pos_x] += 1
    return grid

def part1(commands: tuple[str]) -> int:
    """
    Consider only horizontal and vertical lines. At how many points do at least two lines overlap?


    """
    ocean_floor = _make_grid(1000)
    for command in commands:
        positions = _extract_start_end(command)
        if positions[0] == positions[2] or positions[1] == positions[3]:
            vent = _describe_vent(*positions)
            ocean_floor = _update_ocean_floor(ocean_floor, vent)
    overlap = sum(1 for row in ocean_floor for x in row if x>1)
    return overlap

def part2(commands: tuple[str]) -> int:
    """
    Consider all of the lines. At how many points do at least two lines overlap?


    """
    ocean_floor = _make_grid(1000)
    for command in commands:
        vent = _describe_vent(*_extract_start_end(command))
        ocean_floor = _update_ocean_floor(ocean_floor, vent)
    overlap = sum(1 for row in ocean_floor for x in row if x>1)
    return overlap

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2021_5.txt")
    print(part1(instructions))
    print(part2(instructions))
