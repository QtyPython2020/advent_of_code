# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    """
    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd),
    or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one
    of the other requirements.


    Parameters
    ----------
    commands : str
        The puzzle input.

    Returns
    -------
    nice_strings : int
        The number of nice strings.

    """
    nice_strings = 0
    for command in commands:
        # at least three vowels
        if sum(map(command.count,
                   "aieou")
               ) < 3:
            continue
        # one letter appearing twice in a row
        for last, letter in zip(command[:-1], command[1:]):
            if last == letter:
                break
        else:
            continue
        # not containing
        if sum(map(command.count,
                   ["ab", "cd", "pq", "xy"])
               ) > 0:
            continue
        nice_strings += 1
    return nice_strings

def part2(commands: str):
    """
    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
    but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.

    How many strings are nice under these new rules?

    Parameters
    ----------
    commands : str
        The puzzle input.

    Returns
    -------
    nice_strings : TYPE
        The number of nice strings.

    """
    nice_strings = 0
    for command in commands:
        # pair of two letters that appear at least twice without overlapping
        if any(command[i:i+2] in command[i+2:] for i in range(len(command)-1))\
            and any(command[i]==command[i+2] for i in range(len(command)-2)):
            # one repeating letter with another letter in between
            nice_strings += 1
    return nice_strings

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2015_5.txt")
    print(part1(instructions))
    print(part2(instructions))
