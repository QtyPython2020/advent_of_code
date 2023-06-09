# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

def read_single_line_to_str(path: str) -> str:
    """


    Parameters
    ----------
    path : str
        path to the input file.

    Returns
    -------
    content : str
        the input for the puzzle.

    """
    with open(path, "r") as file:
        puzzle_input = file.readline().rstrip("\n")
    return puzzle_input

def read_multiple_lines_to_list_of_str(path: str):
    with open(path, "r") as file:
        puzzle_input = tuple(line.rstrip("\n") for line in file.readlines())
    return puzzle_input

if __name__ == "__main__":
    pass
