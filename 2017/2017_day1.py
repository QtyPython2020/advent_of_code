# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_str

def part1(captcha: str):
    """
    What is the solution to your captcha?
    """
    digits = ""
    for index, letter in enumerate(captcha):
        if captcha[index-1] == letter:
            digits += letter
    sum_of_digits = sum(int(d) for d in digits)
    return sum_of_digits

def part2(captcha: str):
    """
    What is the solution to your new captcha?
    """
    digits = ""
    length = len(captcha)
    for index in range(length):
        if captcha[index] == captcha[(index+length//2)%length]:
            digits += captcha[index]
    sum_of_digits = sum(int(d) for d in digits)
    return sum_of_digits

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2017_1.txt")
    print(part1(instructions))
    print(part2(instructions))
