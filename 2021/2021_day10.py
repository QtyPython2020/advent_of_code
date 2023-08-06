# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from functools import reduce
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _process_chunk(chunk: str) -> tuple[list]:
    """
    Check every element in the chunk to see if a matching close is found. If all
    elements are valid return the open ends else break the cycle and return the
    illegal character.
    A list is used to stored all the open characters and when a match is found the last
    open character is removed.
    """
    chars = []
    for element in chunk:
        if element in MATCHES:
            chars.append(element)
        elif element == MATCHES[chars[-1]]:
            chars.pop()
        else:
            return element, []
    return [], chars

def part1(chunks: tuple[str]) -> int:
    """
    What is the total syntax error score for those errors?

    Process all the chucks to get all the illegal characters and then calculate
    the score by sum the value for each character.
    """
    scores = {")": 3,
              "]": 57,
              "}": 1197,
              ">": 25137}
    illegals = [r[0] for r in map(_process_chunk, chunks) if r[0]]
    total_score = sum(scores[i] for i in illegals)
    return total_score

def part2(chunks: tuple[str]) -> int:
    """
    What is the middle score?

    Process all the chucks to get all the open ends. Then calculate the score to
    complete each open end, store it in a list and return the middle score.
    """
    scores = {")": 1,
              "]": 2,
              "}": 3,
              ">": 4}
    open_ends = [r[1] for r in map(_process_chunk, chunks) if r[1]]
    total_score = []
    for end in open_ends:
        score = reduce(lambda x,y: (x*5)+y,
                       [scores[MATCHES[m]] for m in end[::-1]])
        total_score.append(score)
    ranking = sorted(total_score)
    return ranking[len(ranking)//2]

MATCHES = {"(":")",
           "[":"]",
           "{":"}",
           "<":">"}

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2021_10.txt")
    print(part1(instructions))
    print(part2(instructions))
