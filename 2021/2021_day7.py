# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import numpy as np
from helpers.helper_functions import read_single_line_to_list_of_int

def part1(positions: np.ndarray):
    """
    How much fuel must they spend to align to that position?
    """
    consumption = np.inf
    for hor in np.arange(min(instructions)+1,max(instructions)):
        fuel = sum(abs(positions-hor))
        consumption = min([fuel, consumption])
    return consumption

def part2(positions: np.ndarray):
    """
    How much fuel must they spend to align to that position?
    """
    consumption = np.inf
    for hor in np.arange(min(instructions)+1,max(instructions)):
        func = np.vectorize(lambda x: sum(range(abs(x-hor)+1)))
        fuel = sum(func(positions))
        consumption = min([fuel, consumption])
    return consumption

if __name__ == "__main__":
    instructions = np.array(read_single_line_to_list_of_int("input_2021_7.txt"))
    print(part1(instructions))
    print(part2(instructions))
