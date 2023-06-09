# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_str

def _deliver_present(visited_houses: dict,
                     pos_x: int,
                     pos_y: int,
                     move: str):
    """
    First, generate the new location from given move. Update the register either
    by adding one more present if the house is already visited and otherwise note
    the first present. Return the updated register and the new x and y position.

    Parameters
    ----------
    visited_houses : dict
        Register of visited houses.
    pos_x : int
        x position of the house.
    pos_y : int
        y position of the house.
    move : str
        Prescribed move.

    Returns
    -------
    visited_houses : TYPE
        Updated register of visited houses.
    new_pos_x : TYPE
        New x position for Santa (or Robo-Santa).
    new_pos_y : TYPE
        New y position for Santa (or Robo-Santa).

    """
    house_x, house_y = MOVE.get(move)((pos_x, pos_y))
    if (house_x, house_y) in visited_houses:
        visited_houses[(house_x, house_y)] += 1
    else:
        visited_houses[(house_x, house_y)] = 1
    new_pos_x, new_pos_y = house_x, house_y
    return visited_houses, new_pos_x, new_pos_y

def part1(commands: str):
    """
    How many houses receive at least one present?
    Go through all the commands and for each deliver a present.

    Parameters
    ----------
    commands : str
        The total given moves.

    Returns
    -------
    number_of_houses : int
        All the houses with at least one present.

    """
    santa_x, santa_y = 0,0
    houses = {(0,0):1}
    for command in commands:
        houses, santa_x, santa_y =_deliver_present(houses,
                                                   santa_x,
                                                   santa_y,
                                                   command)
    number_of_houses = len(houses)
    return number_of_houses

def part2(commands: str):
    """
    How many houses receive at least one present?
    Go through all the commands and for each deliver a present alternating between
    Santa and Robo-Santa.

    Parameters
    ----------
    commands : str
        The total given moves.

    Returns
    -------
    number_of_houses : int
        All the houses with at least one present.

    """
    santa_x, santa_y = 0,0
    robo_x, robo_y = 0,0
    houses = {(0,0):1}
    for turn, command in enumerate(commands):
        if turn % 2:
            houses, santa_x, santa_y =_deliver_present(houses,
                                                       santa_x,
                                                       santa_y,
                                                       command)
        else:
            houses, robo_x, robo_y =_deliver_present(houses,
                                                     robo_x,
                                                     robo_y,
                                                     command)
    number_of_houses = len(houses)
    return number_of_houses

MOVE = {"<": lambda i: (i[0]-1, i[1]),
        ">": lambda i: (i[0]+1, i[1]),
        "^": lambda i: (i[0], i[1]+1),
        "v": lambda i: (i[0], i[1]-1)}

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2015_3.txt")
    print(part1(instructions))
    print(part2(instructions))
