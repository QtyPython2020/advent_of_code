# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
import networkx as nx
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _make_tunnel_network(scan: tuple[str]) -> nx.DiGraph():
    """
    Make the tunnel network from the provided description with each
    """
    network = nx.DiGraph()
    nx.set_node_attributes(network, 0, "flowrate")
    for row in scan:
        valve, *exits = re.findall(r"([A-Z]{2})", row)
        rate = int(re.findall(".*rate=(\d*)", row)[0])
        if valve in network:
            nx.set_node_attributes(network, {valve: {"flowrate": rate}})
        else:
            network.add_node(valve, flowrate = rate)
        for exit_ in exits:
            network.add_edge(valve, exit_)
    for node in network.nodes:
        nx.set_node_attributes(network, False, "open")
    return network

def part1(commands: str):
    tunnels = _make_tunnel_network(commands)
    nx.draw_networkx(tunnels)
    total_pressure = 0
    position = "AA"
    for _ in range(30):
        total_pressure += 0
    return tunnels

def part2(commands: str):
    return

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2022_16_test.txt")
    print(a:=part1(instructions))
    print(part2(instructions))
