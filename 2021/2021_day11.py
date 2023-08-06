# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import numpy as np
from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def _increase_energy_level(octopusses: np.ndarray) -> np.ndarray:
    """
    Start by increasing the energy level of all octopusses. Then while keeping track
    of which octopusses have flashed work out the result of the spill over of the flashes.
    """
    # add one to every octopus
    octopusses += 1
    flashed = []
    # keep working until there are no octopusses with an energy level of 9
    while np.where(octopusses > 9)[0].size:
        # get all the flashes and add them to the list
        new_flashes = list(zip(*np.where(octopusses > 9)))
        flashed.extend(new_flashes)
        # reset the flashed octopusses to zero
        octopusses = np.where(octopusses > 9, 0, octopusses)
        # work out the spilllover
        for pos_y, pos_x in new_flashes:
            # determine all valid positions that spill over gets to
            spills = [(a,b)
                     for a in range(pos_y-1,pos_y+2)
                     for b in range(pos_x-1,pos_x+2)
                     if (a,b) not in flashed # octopus must not have flashed
                     and 0 <= a < len(octopusses) # position must be in the grid
                     and 0 <= b < len(octopusses) # position must be in the grid
                     ]
            for spill in spills:
                octopusses[spill[0]][spill[1]] += 1
    return octopusses, len(flashed)

def part1(commands: str):
    """
    How many total flashes are there after 100 steps?
    """
    grid = np.array(commands)
    num_of_flashes = 0
    for _ in range(100):
        grid, flashes = _increase_energy_level(grid)
        # increase the number of flashes
        num_of_flashes += flashes
    return num_of_flashes

def part2(commands: str):
    """
    What is the first step during which all octopuses flash?
    """
    grid = np.array(commands)
    step = 0
    while True:
        step += 1
        grid, _ = _increase_energy_level(grid)
        if np.where(grid == 0)[0].size == grid.size:
            return step
    return grid

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2021_11.txt", "ints")
    print(part1(instructions))
    print(g:=part2(instructions))
