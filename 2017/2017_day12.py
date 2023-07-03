# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
import networkx as nx
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _build_pipe_network(recordings: tuple[str]) -> nx.Graph():
    """
    Make an undirected Graph by getting the connection from every line and then
    connected the start point to all specified end points.
    """
    graph = nx.Graph()
    for record in recordings:
        start, ends = re.findall(r"(\d*)\s<->\s(.*)", record)[0]
        for end in ends.split(", "):
            graph.add_edge(start, end)
    return graph

def part1(commands: tuple[str]) -> int:
    """
    How many programs are in the group that contains program ID 0?

    From the pipe network get the connected component that contains program ID 0 and
    return the length.
    """
    pipe_network = _build_pipe_network(commands)
    wanted_sub_network = [sub for sub in nx.connected_components(pipe_network) if "0" in sub][0]
    return len(wanted_sub_network)

def part2(commands: tuple[str]) -> int:
    """
    How many groups are there in total?

    Return the length of the list of all the connected components.
    """
    pipe_network = _build_pipe_network(commands)
    nr_sub_network = len(list(nx.connected_components(pipe_network)))
    return nr_sub_network

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2017_12.txt")
    print(a:= part1(instructions))
    print(part2(instructions))
