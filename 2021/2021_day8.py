# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str) -> int:
    """
    In the output values, how many times do digits 1, 4, 7, or 8 appear?
    """
    count = 0
    for command in commands:
        patterns = command.split(" | ")[-1].split(" ")
        count += len([p for p in patterns if len(p) in [2,3,4,7,]])
    return count

def part2(commands: str) -> int:
    """
    What do you get if you add up all of the output values?
    """
    count = 0
    for command in commands:
        pattern, output = list(map(lambda s:s.split(" "),command.split(" | ")))
        length = {n:[] for n in (2, 3, 4, 5, 6, 7)}
        for patt in pattern:
            length[len(patt)].append(set(patt))

        numbers = [{}]*10
        # the numbers that only have a unique number of parts
        numbers[1] = length[2][0]
        numbers[4] = length[4][0]
        numbers[7] = length[3][0]
        numbers[8] = length[7][0]
        # all the horizontal parts are in the 2, 3 and 5
        horizontals = length[5][0] & length[5][1] & length[5][2]
        # the top part is the unique difference between the 1 and the 7
        top = length[3][0] - length[2][0]
        # the 0 is the only number with six parts and two horizontals
        numbers[0] = [i for i in length[6] if len(horizontals.intersection(i))==2][0]
        length[6].remove(numbers[0])
        # keep the undefined horizontals
        horizontals.remove(tuple(top)[0])
        # the bottom part is the only horizontal in the number 0
        bottom = numbers[0] & horizontals
        # the remaining part is the middle horizontal
        middle = horizontals - bottom
        # the top left part is a part in the number 4 that is not in 1 or the middle
        top_left = numbers[4] - numbers[1] - middle
        # all horizontals and the parts of the number 1 make number 3
        numbers[3] = [l for l in length[5] if l==(top|middle|bottom|numbers[1])][0]
        length[5].remove(numbers[3])
        # top left and all horizontals are in the number 5
        numbers[5] = [l for l in length[5] if len(l-(top|middle|bottom|top_left))==1][0]
        length[5].remove(numbers[5])
        # the number 2 is the only remaining one
        numbers[2] = length[5][0]
        # the number 9 is a combination of the number 3 and the top left part
        numbers[9] = [l for l in length[6] if len(l-(numbers[3]|top_left))==0][0]
        length[6].remove(numbers[9])
        # the number 6 is the only remaining one
        numbers[6] = length[6][0]

        count += int("".join(list(map(str,[numbers.index(pattern)
                                           for pattern in map(set, output)]))))
    return count

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2021_8.txt")
    print(part1(instructions))
    print(part2(instructions))
