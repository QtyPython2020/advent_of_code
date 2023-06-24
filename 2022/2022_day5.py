# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re

def _split_move(text: str) -> tuple[str]:
    return re.findall(r"move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)", text.rstrip("\n"))[0]

def part1(moves: str, start_setup: dict):
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?


    """
    stacks = dict(start_setup.items())
    for move in moves:
        amount, start, end = _split_move(move)
        for _ in range(int(amount)):
            crate, stacks[start] = stacks[start][0], stacks[start][1:]
            stacks[end] = [crate] + stacks[end]
    return "".join(stacks[stack][0] for stack in stacks)

def part2(moves: str, start_setup: dict):
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?


    """
    stacks = dict(start_setup.items())
    for move in moves:
        amount, start, end = _split_move(move)
        amount = int(amount)
        crates, stacks[start] = stacks[start][:amount], stacks[start][amount:]
        stacks[end] = crates + stacks[end]
    return "".join(stacks[stack][0] for stack in stacks)

if __name__ == "__main__":
    with open("input_2022_5.txt", mode="r", encoding="utf-8") as file:
        input_text = file.readlines()
    places = [input_text[i].rstrip("\n")[1::2][::2].ljust(9, " ") for i in range(8)]
    setup = {crate: [] for crate in input_text[8].split()}
    for place in places:
        for i in range(9):
            if place[i] != " ":
                setup[str(i+1)].append(place[i])
    instructions = tuple(line.rstrip("\n") for line in input_text[10:])
    print(part1(instructions, setup))
    print(part2(instructions, setup))
