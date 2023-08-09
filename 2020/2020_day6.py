# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from functools import reduce

def part1(answers: list[str]) -> int:
    """
    For each group, count the number of questions to which anyone answered "yes".
    What is the sum of those counts?

    To count the number of questions the length of the set of all the answers is taken.
    """
    count = 0
    for answer in answers:
        count += len(set("".join(answer.split("\n"))))
    return count

def part2(answers: str):
    """
    For each group, count the number of questions to which everyone answered "yes".
    What is the sum of those counts?

    To count this number of questions the length of the overlap between all sets of individuals
    answers is taken.
    """
    count = 0
    for answer in answers:
        count += len(reduce(lambda x,y: x&y,
                            map(set,
                                answer.strip().split("\n"))))
    return count

if __name__ == "__main__":
    with open("input_2020_6.txt") as file:
        instructions = "".join(file.readlines()).split("\n\n")
    print(part1(instructions))
    print(part2(instructions))
