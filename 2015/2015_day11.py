# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_str

def _increment(literal: str, pos: int = None) -> str:
    """
    Increment the password.
    """
    str_length = len(literal)
    if pos is None:
        pos = str_length - 1
    if literal[pos] != "z":
        return literal[:pos] + chr(ord(literal[pos])+1) + literal[pos+1:]
    if pos == 0:
        return "aa" + literal[pos+1:]
    return _increment(literal[:pos] + "a" + literal[pos+1:], pos-1)

def _check_requirement_1(literal: str) -> bool:
    """
    Passwords must include one increasing straight of at least three letters.
    """
    for index, letter in enumerate(literal[:-2]):
        if [ord(l)-ord(letter) for l in literal[index:index+3]] == [0,1,2]:
            return True
    return False

def _check_requirement_2(literal: str) -> bool:
    """
    Passwords may not contain the letters i, o, or l.
    """
    return all(not letter in literal for letter in ["i", "o", "l"])

def _check_requirement_3(literal: str) -> bool:
    """
    Passwords must contain at least two different, non-overlapping pairs of letters.

    """
    pairs = {literal[index:index+2]: index for index, letter in enumerate(literal[:-1])
             if letter==literal[index+1]}
    if pairs == {} or len(pairs) == 1:
        return False
    return True

def _find_new_password(old_password: str) -> str:
    """
    Keep incrementing the password until all three requirements are met.
    """
    password = old_password
    while True:
        # increment the password
        password = _increment(password)
        if all([_check_requirement_1(password),
                _check_requirement_2(password),
                _check_requirement_3(password)]):
            return password

def part1(password: str) -> str:
    """
    Find a new password that meets the requirements.
    """
    return _find_new_password(password)

def part2(password: str) -> str:
    """
    Find another password.
    """
    return _find_new_password(password)

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2015_11.txt")
    print(new_password := part1(instructions))
    print(part2(new_password))
