# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import hashlib
from helpers.helper_functions import read_single_line_to_str

def _test_md5_hash(letters: str,
                   prefix: str) -> int:
    """
    In a loop increasingly find the lowest number to provide a hash with the desired
    number of zeroes.

    Parameters
    ----------
    letters : str
        The puzzle input.
    prefix : str
        The desired first numbers of the hash.

    Returns
    -------
    count : int
        The lowest number.

    """
    count = 100000
    while True:
        str2hash = f"{letters}{count}"
        encoding = str2hash.encode()
        result = hashlib.md5(encoding)
        md5hash = result.hexdigest()
        if md5hash.startswith(prefix):
            return count
        count += 1

def part1(commands: str):
    """
    Find a hash that start with five zeroes.

    Parameters
    ----------
    commands : str
        The puzzle input.

    Returns
    -------
    answer : int
        The lowest number to give the desired hash.

    """
    answer = _test_md5_hash(commands, "00000")
    return answer

def part2(commands: str):
    """
    Find a hash that start with six zeroes.

    Parameters
    ----------
    commands : str
        The puzzle input.

    Returns
    -------
    answer : int
        The lowest number to give the desired hash.

    """
    answer = _test_md5_hash(commands, "000000")
    return answer

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2015_4.txt")
    print(part1(instructions))
    print(part2(instructions))
