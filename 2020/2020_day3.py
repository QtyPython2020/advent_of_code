# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from math import prod
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _traverse(grid: tuple[str],
              right: str,
              down: str) -> int:
    """
    Count the number of times a tree is encountered by stepping through the grid by rows.
    From the row calculate the step down and step right on the input.
    """
    return sum(grid[(pos)%len(grid)][(pos//down*right)%len(grid[0])]=="#"
               for pos in range(0,len(grid),down))

def part1(area: tuple[str]) -> int:
    """
    Starting at the top-left corner of your map and following a slope of right 3 and down 1,
    how many trees would you encounter?
    """
    trees = _traverse(area, 3, 1)
    return trees

def part2(area: tuple[str]) -> int:
    """
    What do you get if you multiply together the number of trees encountered on each of the
    listed slopes?
    """
    trees = [_traverse(area, 1, 1),
             _traverse(area, 3, 1),
             _traverse(area, 5, 1),
             _traverse(area, 7, 1),
             _traverse(area, 1, 2)]
    return prod(trees)

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2020_3.txt")
    print(part1(instructions))
    print(part2(instructions))
