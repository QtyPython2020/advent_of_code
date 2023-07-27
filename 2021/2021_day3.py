# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from typing import Callable
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str) -> int:
    """
    What is the power consumption of the submarine?

    First make the binary number by finding the most common in every position of the
    provided numbers. Create an inverted number. Turn both binary numbers into decimal
    numbers and return the product.
    """
    #
    gamma_str = ""
    for length in range(len(commands[0])):
        numbers = "".join([c[length] for c in commands])
        counts = [("1", numbers.count("1")), ("0",numbers.count("0"))]
        gamma_str += max(counts, key=lambda x:x[1])[0]
    #
    b_dict = {'0': '1', '1': '0'}
    epsilon_str = ""
    for i in gamma_str:
        epsilon_str += b_dict[i]
    #
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)
    consumption = gamma * epsilon
    return consumption

def _find_remaining_number(numbers: tuple[str],
                           func: Callable,
                           val: str) -> str:
    """
    Find the remaining number by weeding out numbers that do not fit the criteria.
    The bit criteria is determined by the func and the val. Apply the filter until only
    one number is left and return that number.
    """
    start = ""
    for length in range(len(numbers[0])):
        column = "".join([c[length] for c in numbers])
        counts = [("1", column.count("1")), ("0",column.count("0"))]
        common = func(counts, key=lambda x:x[1])
        value = val if counts[0][1] == counts[1][1] else common[0]
        start += value
        numbers = [num for num in numbers if num.startswith(start)]
        if len(numbers) == 1:
            break
    return numbers[0]

def part2(commands: str) -> int:
    """
    What is the life support rating of the submarine?

    Find the binary number for each rating, turn them into decimal numbers and return the product.
    """
    oxygen_rating = int(_find_remaining_number(commands, max, "1"), 2)
    co2_rating = int(_find_remaining_number(commands, min, "0"), 2)
    life_support_rating = oxygen_rating * co2_rating
    return life_support_rating

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2021_3.txt")
    print(part1(instructions))
    print(part2(instructions))
