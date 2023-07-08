# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
import networkx as nx
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

class Worker:
    """
    Human or elf worker that gets a step, determines the duration and then executes it.
    """
    def __init__(self):
        self.time = 0
        self.step = None

    def get_step(self, step:str):
        """
        From a provided step determine the duration and note down the step.
        """
        self.time = (ord(step)-4)
        self.step = step

    def tick(self):
        """
        Decrease one time step
        """
        self.time = max(self.time-1, 0)

def _build_requirement_tree(requirements: tuple[str]) -> nx.DiGraph():
    """
    Make a directed graph from the list of requirements by extract the two steps
    and creating a directed edge between them.
    """
    graph = nx.DiGraph()
    for requirement in requirements:
        before, after = re.findall(r"Step\s([A-Z]).*([A-Z])", requirement)[0]
        graph.add_edge(before, after)
    return graph

def _find_first_steps(graph: nx.DiGraph()) -> list[str]:
    """
    Find the first steps by looking for nodes that have an indegree of 0 i.e. they
    have no required steps to start.
    """
    in_degrees = nx.in_degree_centrality(graph)
    first_nodes = sorted([node for node, value in in_degrees.items() if value==0])
    return first_nodes


def _determine_available_steps(graph: nx.DiGraph(),
                               next_steps: list[str],
                               order_so_far: str,
                               available: list[str]) -> list:
    """
    For each provided next step check whether all the requirements are met i.e. they are in noted
    order thus far. In that case add them to the list of available next steps and return a sorted
    list of all available next steps.
    """
    for next_step in next_steps:
        # find the requirements for the next step
        must_have_finished = [edge[0] for edge in graph.edges if edge[1]==next_step]
        #
        for previous in must_have_finished:
            if previous not in order_so_far:
                break
        else:
            available += next_step
    return sorted(available)

def part1(commands: str) -> str:
    """
    In what order should the steps in your instructions be completed?

    Starting from the root complete one step, check what the new options are, take the
    first one based on lexigraphical order and repeat until all steps are done.
    """
    tree = _build_requirement_tree(commands)
    stack = _find_first_steps(tree)
    root = stack.pop(0)
    order = ""
    # traverse the tree from the root
    while len(order) < tree.order():
        order += root
        stack = _determine_available_steps(tree, tree[root], order, stack)
        if stack == []:
            break
        root = stack.pop(0)
    return order

def part2(commands: str, num_of_workers: int) -> int:
    """
    With 5 workers and 60+ seconds duration per step, how long will it take to complete
    all of the steps?

    ?
    """
    tree = _build_requirement_tree(commands)
    workers = [Worker() for _ in range(num_of_workers)]
    stack = _find_first_steps(tree)
    order = ""
    second = -1
    while stack or any(worker.time > 0 for worker in workers):
        for worker in workers:
            # decrement remaining time
            worker.tick()
            # if task complete, give new task
            if worker.time == 0:
                if worker.step is not None:
                    order += worker.step
                    stack = _determine_available_steps(tree, tree[worker.step], order, stack)
                    worker.step = None
                if stack:
                    worker.get_step(stack.pop(0))
        # next time increment
        second += 1
    return second

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_7.txt")
    print(part1(instructions)) #ACBDESULXKYZIMNTFGWJVPOHRQ
    print(part2(instructions, num_of_workers=5)) #980
