# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import json

def read_single_line_to_str(path: str) -> str:
    """

    """
    with open(path, "r") as file:
        puzzle_input = file.readline().rstrip("\n")
    return puzzle_input

def read_single_line_to_json(path: str):
    with open(path, "r") as file:
        puzzle_input = json.loads(file.read())
    return puzzle_input

def read_multiple_lines_to_tuple_of_str(path: str) -> tuple[str]:
    """

    """
    with open(path, "r") as file:
        puzzle_input = tuple(line.rstrip("\n") for line in file.readlines())
    return puzzle_input

if __name__ == "__main__":
    pass
