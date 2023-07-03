# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

class Program:
    def __init__(self, name, weight=0, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = None
        self.subsums = None
        self.even = None

    def update_weight(self, weight):
        self.weight = weight

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def add_parent(self, parent):
        """

        """
        self.parent = parent

    def sum_weight_children(self):
        """

        """
        if self.children is None:
            return self.weight
        self.subsums = []
        for child in self.children:
            self.subsums.append(child.sum_weight_children())
        self.determine_even()
        return sum(self.subsums, self.weight)

    def determine_even(self):
        """
        Set even to True if all the children have equal weight
        """
        self.even = len(set(self.subsums)) == 1

    def find_unbalance(self):
        if self.even or self.subsums is None:
            return
        a,b,c = self.subsums
        if set([a]) not in set([b,c]):
            pos = 0
            difference = a - b
        elif set([b]) not in set([a,c]):
            pos = 1
            difference = b - a
        else:
            pos = 2
            difference = c - a
        to_be_corrected = self.children[pos].weight - difference
        return to_be_corrected

def _load_all_files(listings: tuple[str]) -> dict:
    """

    """
    programs = {}
    for listing in listings:
        filename, weight, rest = re.findall(r"(\w*)\s\((\d*)\)\s?-?>?\s?(.*)", listing)[0]
        if filename not in programs:
            programs.update({filename: Program(filename, int(weight))})
        if filename in programs and programs[filename].weight == 0:
            programs[filename].update_weight(int(weight))
        if rest:
            for file in rest.split(", "):
                if file not in programs:
                    subfile = Program(file, parent=filename)
                    programs.update({file: subfile})
                    programs[filename].add_child(subfile)
                else:
                    programs[file].add_parent(filename)
                    programs[filename].add_child(programs[file])
    return programs

def part1(commands: str):
    """

    """
    file_tower = _load_all_files(commands)
    return [p.name for p in file_tower.values() if p.parent is None][0]

def part2(commands: str, root: str):
    """
    Given that exactly one program is the wrong weight, what would its weight need to be to
    balance the entire tower?


    """
    file_tower = _load_all_files(commands)
    file_tower[root].sum_weight_children()
    for file in file_tower:
        new_weight = file_tower[file].find_unbalance()
        if new_weight:
            break
    return new_weight

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2017_7.txt")
    print(top:= part1(instructions))
    print(part2(instructions, top)) #answer is 256
