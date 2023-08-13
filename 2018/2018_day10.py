# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    lst = []
    for command in commands:
        coord_x, coord_y, vel_x, vel_y = list(map(int,
                                                  re.findall(r"([\s|-]?\d+)",
                                                             command)
                                                  )
                                              )
        lst.append({"x": coord_x,
                    "y": coord_y,
                    "vel_x": vel_x,
                    "vel_y": vel_y})
    min_x = min(l["x"] for l in lst)
    max_x = max(l["x"] for l in lst)
    min_y = min(l["y"] for l in lst)
    max_y = max(l["y"] for l in lst)
    x_axis = max_x - min_x + 1
    y_axis = max_y - min_y + 1
    print(x_axis, y_axis)
    # #
    for _ in range(1):
        grid = [["." for _ in range(x_axis)] for _ in range(y_axis)]
        for i, l in enumerate(lst):
            grid[l["y"]+abs(min_y)][l["x"]+abs(min_x)] = "#"
            new_x = l["x"] + l["vel_x"]
            new_y = l["y"] + l["vel_y"]
            lst[i] = {"x": new_x,
                  "y": new_y,
                  "vel_x": l["vel_x"],
                  "vel_y": l["vel_y"]}
        for row in grid:
            print("".join(x for x in row))
        print()
    return

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_10.txt")
    print(part1(instructions[:100]))
    print(part2(instructions))
