# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_single_line_to_dict_of_int

def part1(memory: str):
    """
    How many redistribution cycles must be completed before a configuration is produced that has been seen before?
    """
    memory_banks = list(memory.keys())
    length = len(memory_banks)
    previous = []
    configuration = ""
    steps = 0
    while True:
        steps += 1
        max_stack = sorted(memory.items(),
                           key=lambda x:x[1],
                           reverse=True)[0][0]
        blocks = memory[max_stack]
        memory[max_stack] = 0
        index = memory_banks.index(max_stack) + 1
        for _ in range(blocks):
            memory[index%length] += 1
            index += 1
        configuration = "".join(str(el) for el in memory.values())
        if configuration in previous:
            break
        previous.append(configuration)
    return steps

def part2(memory: str):
    pass

if __name__ == "__main__":
    instructions = read_single_line_to_dict_of_int("input_2017_6.txt")
    print(part1(instructions))
    print(part2(instructions))
