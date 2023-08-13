# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
import networkx as nx
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _make_tunnel_network(scan: tuple[str]) -> nx.DiGraph():
    network = nx.DiGraph()
    for row in scan:
        valve, *exits = re.findall(r"([A-Z]{2})", row)
        rate = re.findall(r"(\d*)", row)
        if valve in network:
            # network[valve]["flowrate"] = rate
            pass
        else:
            network.add_node(valve, flowrate = rate)
        for exit_ in exits:
            network.add_edge(valve, exit_)
    return network

def part1(commands: str):
    tunnels = _make_tunnel_network(commands)
    nx.draw_networkx(tunnels)
    return tunnels

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_16_test.txt")
    print(part1(instructions))
    print(part2(instructions))
