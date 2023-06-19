# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _find_last_key(grid: list[list[str]], key: str) -> tuple[int]:
    """
    Loop through the key pad to find the position of the last key.
    """
    pos_x, pos_y = None, None
    for pos_y, sub_grid in enumerate(grid):
        for pos_x, cell in enumerate(sub_grid):
            if cell == key:
                break
        else:
            continue
        break
    return pos_x, pos_y

def _get_next_key(move: str, keypad: list[list[str]], last_key: str) -> str:
    """
    Based on the old position and the move determine the new position.
    """
    moves = {"R": (1,0),
             "L": (-1,0),
             "U": (0,-1),
             "D": (0,1)}
    old_x, old_y = _find_last_key(keypad, last_key)
    dir_x, dir_y = moves.get(move)
    new_x, new_y = max(0, old_x + dir_x), max(0, old_y + dir_y)
    try:
        outcome= keypad[new_y][new_x]
        key = outcome if outcome != "" else last_key
    except IndexError:
        key = last_key
    return key

def part1(commands: str):
    """
    Your puzzle input is the instructions from the document you found at the
    front desk. What is the bathroom code?
    """
    keypad = [["1","2","3"],
              ["4","5","6"],
              ["7","8","9"]]
    code = ""
    current_key = "5"
    for command in commands:
        for instr in command:
            current_key = _get_next_key(instr,
                                        keypad,
                                        current_key)
        code += current_key
    return code

def part2(commands: str):
    """
    Using the same instructions in your puzzle input, what is the correct bathroom code?
    """
    keypad = [["","","1","",""],
              ["","2","3","4",""],
              ["5","6","7","8","9"],
              ["","A","B","C",""],
              ["","","D","",""]]
    code = ""
    current_key = "5"
    for command in commands:
        for instr in command:
            current_key = _get_next_key(instr,
                                        keypad,
                                        current_key)
        code += current_key
    return code

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2016_2.txt")
    print(part1(instructions))
    print(part2(instructions))
