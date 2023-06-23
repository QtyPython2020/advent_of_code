# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    """
    What would your total score be if everything goes exactly according to your strategy guide?

    For each round check the score:
        - 0 for loss
        - 3 for draw
        - 6 for win
        - 1 for rock
        - 2 for paper
        - 3 for scissors
    """
    score = 0
    result = {("A", "X"): 1+3,
              ("A", "Y"): 2+6,
              ("A", "Z"): 3+0,
              ("B", "X"): 1+0,
              ("B", "Y"): 2+3,
              ("B", "Z"): 3+6,
              ("C", "X"): 1+6,
              ("C", "Y"): 2+0,
              ("C", "Z"): 3+3,
              }
    for command in commands:
        other, mine = command.split()
        score += result.get((other, mine))
    return score

def part2(commands: str):
    """
    What would your total score be if everything goes exactly according to your strategy guide?

    For each round check the score:
        - 0 for loss
        - 3 for draw
        - 6 for win
        - 1 for rock
        - 2 for paper
        - 3 for scissors
    """
    score = 0
    result = {("A", "X"): 3+0,
              ("A", "Y"): 1+3,
              ("A", "Z"): 2+6,
              ("B", "X"): 1+0,
              ("B", "Y"): 2+3,
              ("B", "Z"): 3+6,
              ("C", "X"): 2+0,
              ("C", "Y"): 3+3,
              ("C", "Z"): 1+6,
              }
    for command in commands:
        other, mine = command.split()
        score += result.get((other, mine))
    return score

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_2.txt")
    print(part1(instructions))
    print(part2(instructions))
