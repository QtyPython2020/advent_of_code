# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import json

def read_single_line_to_str(path: str) -> str:
    """
    Read the input from the text file at the provided filepath. The file should
    contain one line and the output will be a string.
    """
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = file.readline().rstrip("\n")
    return puzzle_input

def read_single_line_to_tuple_of_str(path: str) -> tuple[str]:
    """
    Read the input from the text file at the provided filepath. The file should
    contain one line and the output will be a tuple of strings.
    """
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = tuple(file.readline().rstrip("\n").split(", "))
    return puzzle_input

def read_json_to_object(path: str) -> (list,dict):
    """
    Read the input from the text file at the provided filepath. The file should
    contain one json object and the output will be a dictionary or list.
    """
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = json.loads(file.read())
    return puzzle_input

def read_multiple_lines_to_tuple_of_str(path: str) -> tuple[str]:
    """
    Read the input from the text file at the provided filepath. The file should
    contain multiple lines and the output will be a tuple of strings.
    """
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = tuple(line.rstrip("\n") for line in file.readlines())
    return puzzle_input

if __name__ == "__main__":
    pass
