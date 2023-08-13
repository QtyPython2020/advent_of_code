# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

class Bag:
    def __init__(self,
                 color: str,
                 parent = None):
        self.color = color
        self.parent = parent
        self.children = None

    def add_content(self, contents: list):
        if self.children is None:
            self.children = []
        for content in contents.split(", "):
            num, color = re.findall("(\d*)\s(.*)\sbags?", content.rstrip("."))[0]
            for _ in range(int(num)):
                self.children.append(Bag(color, self.color))

    def find_bag(self, bag_type:str):
        if self.children is None:
            return False
        if {c.color for c in self.children if c.color == bag_type}:
            return True
        for child in set(self.children):
            print(child.color)
            return child.find_bag(bag_type)

def part1(rules: tuple[str]):
    """
    How many bag colors can eventually contain at least one shiny gold bag?
    """
    bags = []
    mapping = {}
    for rule in rules:
        parent, contents = re.findall(r"(.*)\sbags\scontain\s(.*)", rule)[0]
        if parent not in mapping:
            bag = Bag(parent)
        if contents != "no other bags.":
            bag.add_content(contents)
            pass
        bags.append(bag)
        mapping.update({bag.color: bags.index(bag)})
    print( [(m.color, 1 if m.children is None else [c.color for c in m.children]) for m in bags])
    return bags

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2020_7_test.txt")
    from pprint import pprint
    pprint(b:=part1(instructions))
    print(part2(instructions))
