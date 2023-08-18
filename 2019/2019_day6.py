# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import networkx as nx
from helpers.helper_functions import read_multiple_lines_to_tuple_of_parsed_element

def _make_universe(descriptions: tuple[tuple[str]]):
    """
    Make a directed acyclic graph from the provided orbits.
    """
    orbits = nx.DiGraph()
    for description in descriptions:
        center, obj = description
        orbits.add_edge(center, obj)
    return orbits

def part1(orbits: tuple[tuple[str]]):
    """
    What is the total number of direct and indirect orbits in your map data?

    Make the described universe and then calculate the sum of shortest paths discounting
    the end point.
    """
    universe = _make_universe(orbits)
    num = sum(len(nx.shortest_path(universe, "COM", node))-1 for node in universe.nodes)
    return num


def part2(orbits: tuple[tuple[str]]):
    """
    What is the minimum number of orbital transfers required to move from the object
    YOU are orbiting to the object SAN is orbiting?

    """
    universe = _make_universe(orbits)
    your_orbits = nx.shortest_path(universe, "COM", "YOU")
    santas_orbits = nx.shortest_path(universe, "COM", "SAN")
    for you,san in zip(your_orbits,santas_orbits):
        if you!=san:
            i=your_orbits.index(you)
            break
    moves = len(your_orbits[i:])-1 +  len(santas_orbits[i:])-1
    return moves

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_parsed_element("input_2019_6.txt",
                                                                  "str",
                                                                  sep=")")
    print(part1(instructions))
    print(part2(instructions))
