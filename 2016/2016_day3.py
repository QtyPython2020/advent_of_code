# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def _check_possible_triangle(sides: tuple):
    """
    Determine of a triangle is possible which is if the sum of any two sides is larger
    than the remaining side
    """
    side_a, side_b, side_c = sorted(sides)
    return (side_a + side_b) > side_c

def part1(commands: str):
    """
    How many of the listed triangles are possible?
    """
    possible_triangles = sum(_check_possible_triangle(command) for command in commands)
    return possible_triangles

def part2(commands: str):
    """
    How many of the listed triangles are possible if the orientation of reading is changed?
    """
    possible_triangles = 0
    for col in range(3):
        for row in range(0, len(commands), 3):
            possible_triangles += _check_possible_triangle((commands[row][col],
                                                            commands[row+1][col],
                                                            commands[row+2][col]))
    return possible_triangles

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2016_3.txt",
                                                                  "int")
    print(part1(instructions))
    print(part2(instructions))
