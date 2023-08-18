# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _looper(stuff, num_cycle):
    program = list(stuff)
    register = 1
    current = None
    for _ in range(num_cycle):
        if current is None:
            current = program.pop(0)
            if current == "noop":
                current = None
        else:
            register += int(current.strip("addx "))
            current = None
    return register

def part1(commands: str):
    """
    What is the sum of these six signal strengths?
    """
    total = sum((_looper(commands, i)*i for i in [20,60,100,140,180,220]))
    return total

def part2(commands: str):
    """
    What eight capital letters appear on your CRT?
    """
    program = list(commands)
    x = 1
    current = None
    screen = [["" for i in range(40)] for j in range(6)]
    sprite = (0,1,2)
    for cycle in range(240):
        screen[cycle//40][cycle%40] = "#" if cycle%40 in sprite else "."
        if current is None:
            current = program.pop(0)
            if current == "noop":
                current = None
        else:
            x += int(current.strip("addx "))
            sprite = (x-1,x,x+1)
            current = None
    for row in screen:
        print("".join(map(str,row)))

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_10.txt")
    print(part1(instructions))
    print(part2(instructions))
