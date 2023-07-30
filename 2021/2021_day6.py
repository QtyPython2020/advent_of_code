# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from helpers.helper_functions import read_single_line_to_list_of_int

def _create_starting_point(original: list[int]) -> dict:
    """
    From the provided list make a dict with the number of lanternfish per stage.
    """
    return {i:list(original).count(i) for i in range(0,9)}

def _simulate_fish(old_fishes: dict)->dict:
    """
    Run the simulation by creating a new dictionary where every staged is decreased by 1.
    Then the amount of lanternfishes that were in stage 0 are added the stage 6 and an equal
    amount of new fishes are added.
    """
    new = {i:old_fishes[i+1] for i in range(0,8)}
    new[6] += (spawn := old_fishes[0])
    new[8] = spawn
    return new

def part1(start_point: list[int]) -> int:
    """
    How many lanternfish would there be after 80 days?
    """
    fishes = _create_starting_point(start_point)
    for _ in range(80):
        fishes = _simulate_fish(fishes)
    return sum(fishes.values())

def part2(start_point: list[int]) -> int:
    """
    How many lanternfish would there be after 256 days?

    """
    fishes = _create_starting_point(start_point)
    for _ in range(256):
        fishes = _simulate_fish(fishes)
    return sum(fishes.values())

if __name__ == "__main__":
    instructions = read_single_line_to_list_of_int("input_2021_6.txt")
    print(part1(instructions))
    print(part2(instructions))
