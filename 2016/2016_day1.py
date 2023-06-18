# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_single_line_to_tuple_of_str

def _extract_turn_and_walk(instruction: str,
                           old_x: int,
                           old_y: int) -> tuple[int, int, int]:
    """
    From the instruction extract the turn to take and the distance to walk. Based
    on the turn and the old direction return the new direction.
    """
    turn, walk = re.findall(r"([R|L])(\d*)",
                            instruction)[0]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    index = (directions.index((old_x, old_y)) + (1 if turn == "R" else -1))%4
    new_x, new_y = directions[index]
    return new_x, new_y, int(walk)

def part1(commands: str) -> int:
    """
    How far is the shortest path to the destination?
    """
    pos_x, pos_y = (0,0)
    dir_x, dir_y = (0,1)
    for command in commands:
        dir_x, dir_y, walk = _extract_turn_and_walk(command, dir_x, dir_y)
        pos_x = pos_x + dir_x * walk
        pos_y = pos_y + dir_y * walk
    euclidean_distance = abs(pos_x) + abs(pos_y)
    return euclidean_distance

def part2(commands: str) -> int:
    """
    How many blocks away is the first location you visit twice?
    """
    positions = []
    pos_x, pos_y = (0,0)
    dir_x, dir_y = (0,1)
    for command in commands:
        dir_x, dir_y, walk = _extract_turn_and_walk(command, dir_x, dir_y)
        for _ in range(walk):
            pos_x = pos_x + dir_x
            pos_y = pos_y + dir_y
            # if the position has been visited already stop walking
            if (pos_x, pos_y) in positions:
                break
            positions.append((pos_x, pos_y))
        # if no earlier visited position is found the walk will go on to the next instruction
        else:
            continue
        # if an earlier visited position is found no new instruction will be followed
        break
    euclidean_distance = abs(pos_x) + abs(pos_y)
    return euclidean_distance

if __name__ == "__main__":
    instructions = read_single_line_to_tuple_of_str("input_2016_1.txt")
    print(part1(instructions))
    print(part2(instructions))
