# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    instructions = []
    register = {"a":0, "b":0}
    pos = 0
    for command in commands:
        instr, reg, other = re.findall("(\w{,3})\s(a|b|.\d{,2}),?\s?(.\d{,2})?", command)[0]
        instructions.append((instr, reg, other))
    while True:
        if pos > len(instructions)-1:
            break
        if instructions[pos][0] == "hlf":
            register[instructions[pos][1]] /= 2
            pos += 1
        elif instructions[pos][0] == "tpl":
            register[instructions[pos][1]] *= 3
            pos += 1
        elif instructions[pos][0] == "inc":
            register[instructions[pos][1]] += 1
            pos += 1
        elif instructions[pos][0] == "jmp":
            pos += int(instructions[pos][1])
        elif instructions[pos][0] == "jie":
            if register[instructions[pos][1]]%2 == 0:
                pos += int(instructions[pos][2])
            else:
                pos += 1
        elif instructions[pos][0] == "jio":
            if register[instructions[pos][1]] == 1:
                pos += int(instructions[pos][2])
            else:
                pos += 1
    return register["b"]

def part2(commands: str):
    instructions = []
    register = {"a":1, "b":0}
    pos = 0
    for command in commands:
        instr, reg, other = re.findall("(\w{,3})\s(a|b|.\d{,2}),?\s?(.\d{,2})?", command)[0]
        instructions.append((instr, reg, other))
    while True:
        if pos > len(instructions)-1:
            break
        if instructions[pos][0] == "hlf":
            register[instructions[pos][1]] /= 2
            pos += 1
        elif instructions[pos][0] == "tpl":
            register[instructions[pos][1]] *= 3
            pos += 1
        elif instructions[pos][0] == "inc":
            register[instructions[pos][1]] += 1
            pos += 1
        elif instructions[pos][0] == "jmp":
            pos += int(instructions[pos][1])
        elif instructions[pos][0] == "jie":
            if register[instructions[pos][1]]%2 == 0:
                pos += int(instructions[pos][2])
            else:
                pos += 1
        elif instructions[pos][0] == "jio":
            if register[instructions[pos][1]] == 1:
                pos += int(instructions[pos][2])
            else:
                pos += 1
    return register["b"]

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2015_23.txt")
    print(part1(instructions))
    print(part2(instructions))
