# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from math import floor
from helpers.helper_functions import read_multiple_lines_to_list_of_ints

def _calculate_fuel(mass: int) -> int:
    """

    """
    return floor(mass/3)-2

def part1(rockets: str) -> int:
    """
    What is the sum of the fuel requirements for all of the modules on your spacecraft?


    """
    total = 0
    for rocket_mass in rockets:
        total += _calculate_fuel(rocket_mass)
    return total

def part2(rockets: str) -> int:
    """
    What is the sum of the fuel requirements for all of the modules on your spacecraft
    when also taking into account the mass of the added fuel?


    """
    total = 0
    for rocket_mass in rockets:
        sub_total = 0
        while True:
            rocket_mass = _calculate_fuel(rocket_mass)
            sub_total += rocket_mass
            if rocket_mass < 6:
                break
        total += sub_total
    return total

if __name__ == "__main__":
    instructions = read_multiple_lines_to_list_of_ints("input_2019_1.txt")
    print(part1(instructions))
    print(part2(instructions))
