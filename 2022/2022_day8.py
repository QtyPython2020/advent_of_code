# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def part1(forrest: str):
    """
    How many trees are visible from outside the grid?


    """
    visible = 0
    for loc_y, row_of_trees in enumerate(forrest):
        for loc_x, tree in enumerate(row_of_trees):
            # all trees on the outside are visible
            if loc_x in (0,4) or loc_y in (0,4):
                visible += 1
                continue
            # check left and right
            if all(tree > other for other in row_of_trees[:loc_x]) or \
                all(tree > other for other in row_of_trees[loc_x+1:]):
                visible += 1
                continue
            # check top and bottom
            if all(tree > row[loc_x] for row in forrest[:loc_y]) or \
                all(tree > row[loc_x] for row in forrest[loc_y+1:]):
                visible += 1
                continue
    return visible

def part2(forrest: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2022_8.txt",
                                                                  "ints")
    print(part1(instructions))
    print(part2(instructions))
# ((3,0,3,7,3),(2,5,5,1,2),(6,5,3,3,2),(3,3,5,4,9),(3,5,3,9,0))
