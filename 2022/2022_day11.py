# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from numpy import prod

class Monkey:
    """
    Make a Monkey object to represent the monkey that has a list of items, an operation
    for the worry level, a test and two options to pass the item.
    """
    def __init__(self, name, notes: list[str]):
        self.name = name
        self.items = list(map(int,
                              notes[0].split(": ")[-1].split(", ")))
        elements = re.findall(r"=\s(.*)\s([+*])\s(.*)",
                              notes[1].split(": ")[-1])[0]
        string = f"lambda old: {elements[0]}{elements[1]}{elements[-1]}"
        self.operation = eval(string)
        self.test = int(re.findall(r"by\s(\d*)",
                                   notes[2])[0])
        self.option1 = int(re.findall(r"monkey\s(\d*)",
                                      notes[3])[-1])
        self.option2 = int(re.findall(r"monkey\s(\d*)",
                                      notes[4])[-1])
        self.items_inspected = 0

    def update_option(self, others):
        """
        Replace the numbers of the monkeys with the actual objects
        """
        self.option1 = others[self.option1]
        self.option2 = others[self.option2]

    def take_item(self, item):
        """
        Receive an item and place it on the monkey's list
        """
        self.items.append(item)

def part1(commands: str):
    """
    What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
    """
    lst = [Monkey(n, description.split("\n")[1:]) for n, description in enumerate(commands)]
    for monkey in lst:
        monkey.update_option(lst)
    for _ in range(20):
        for monkey in lst:
            while monkey.items:
                monkey.items_inspected += 1
                item = monkey.items.pop(0)
                worry_level = monkey.operation(item) // 3
                if worry_level%monkey.test == 0:
                    monkey.option1.take_item(worry_level)
                else:
                    monkey.option2.take_item(worry_level)
    return prod(sorted([l.items_inspected for l in lst])[-2:])

def part2(commands: str):
    """
    What is the level of monkey business after 10000 rounds?
    """
    return

if __name__ == "__main__":
    with open("input_2022_11_test.txt", encoding="utf-8") as file:
        instructions = file.read().split("\n\n")
    print(part1(instructions))
    print(part2(instructions))
