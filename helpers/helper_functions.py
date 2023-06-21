# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import json
import re
from typing import Union, Any

def _parse_to_int(element: str) -> tuple[int]:
    """
    Extract all numeric element and convert these to integers
    """
    return tuple(int(el) for el in re.findall(r"(\d{1,})", element))

def _parse_to_str(element: str, sep: str = None) -> tuple[str]:
    """
    Extract all seperate elements from string and convert these to strings
    """
    return tuple(element.split(sep=sep))

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

def read_single_line_to_dict_of_int(path: str) -> dict[int]:
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = {index: int(el) for index, el in enumerate(file.readline().rstrip("\n").split())}
    return puzzle_input

def read_json_to_object(path: str) -> Union[list, dict]:
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
        puzzle_input = tuple(line.rstrip("\n")
                             for line in file.readlines())
    return puzzle_input

def read_multiple_lines_to_tuple_of_parsed_element(path: str,
                                                   parser: str) -> tuple[Any]:
    """
    Read the input from the text file at the provided filepath. The file should
    contain multiple lines and the output will be a tuple of any type based on
    the provided parse specification.
    """
    func = PARSERS.get(parser)
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = tuple(func(line.rstrip("\n")) for line in file.readlines())
    return puzzle_input

def read_multiple_lines_to_list_of_ints(path: str):
    """

    """
    with open(path, mode="r", encoding="utf-8") as file:
        puzzle_input = [int(line.rstrip("\n")) for line in file.readlines()]
    return puzzle_input

PARSERS = {"int": _parse_to_int,
           "str": _parse_to_str}

if __name__ == "__main__":
    pass
