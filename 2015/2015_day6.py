# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _make_grid():
    """
    Make a 1000x1000 grid filled with 0's.

    Returns
    -------
    grid : list[list[int]]
        The starting grid.

    """
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    return grid

def _extract_instruction_and_coordinates(line: str):
    """
    Extract the instructions and the integer coordinates from the command.

    Parameters
    ----------
    line : str
        The command.

    Returns
    -------
    task : str
        The action to be taken.
    int_coords: list[int]
        Unpacking of a list of integers.

    """
    task, *coords = re.findall(r"(.*)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)",
                                      line)[0]
    int_coords = [int(el) for el in coords]
    return task, *int_coords

def part1(commands: str):
    """
    How many lights are lit?

    Parameters
    ----------
    commands : str
        The instructions for the lights.

    Returns
    -------
    number_of_lights_lit : int
        The number of lights lit.

    """
    grid = _make_grid()
    for command in commands:
        action, start_x, start_y, end_x, end_y = _extract_instruction_and_coordinates(command)
        if action == "turn on":
            for row in range(start_x, end_x+1):
                for col in range(start_y, end_y+1):
                    grid[row][col] = 1
        elif action == "turn off":
            for row in range(start_x, end_x+1):
                for col in range(start_y, end_y+1):
                    grid[row][col] = 0
        elif action == "toggle":
            for row in range(start_x, end_x+1):
                for col in range(start_y, end_y+1):
                    grid[row][col] = sum([not grid[row][col]])
    number_of_lights_lit = sum(cell for row in grid for cell in row)
    return number_of_lights_lit

def part2(commands: str):
    """
    What is the total brightness of all lights combined after following Santa's instructions?

    Parameters
    ----------
    commands : str
        The instructions for the lights.

    Returns
    -------
    number_of_lights_lit : int
        The total brightness.

    """
    grid = _make_grid()
    for command in commands:
        action, start_x, start_y, end_x, end_y = _extract_instruction_and_coordinates(command)
        if action == "turn on":
            for row in range(start_x, end_x+1):
                for col in range(start_y, end_y+1):
                    grid[row][col] += 1
        elif action == "turn off":
            for row in range(start_x, end_x+1):
                for col in range(start_y, end_y+1):
                    if grid[row][col] >= 1:
                        grid[row][col] -= 1
                    else:
                        pass
        elif action == "toggle":
            for row in range(start_x, end_x+1):
                for col in range(start_y, end_y+1):
                    grid[row][col] += 2
    number_of_lights_lit = sum(cell for row in grid for cell in row)
    return number_of_lights_lit

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2015_6.txt")
    print(part1(instructions))
    print(part2(instructions))
