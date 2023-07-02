# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from itertools import permutations
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _parse_distances(distances: tuple[str]) -> tuple[dict, set]:
    """
    With a regex extract the cities and the travel distance. From this create a dictionary with
    all the possible routes and their distance.
    """
    travels = {}
    cities = set()
    for distance in distances:
        start, end, length = re.findall(r"(\w*)\sto\s(\w*)\s=\s(\d*)", distance)[0]
        travels.update({f"{start}-{end}": int(length)})
        travels.update({f"{end}-{start}": int(length)})
        cities.add(start)
        cities.add(end)
    return travels, cities

def _get_all_trip_lengths(routes: tuple[str]) -> set:
    """
    Go through all the possible combinaties of seeing all cities and sum up the total distance of
    the trip. Make a set of all the distances.
    """
    distances, destinations = _parse_distances(routes)
    total_distances = set()
    for combination in permutations(destinations):
        trip_total = 0
        for city1, city2 in zip(combination[:-1],combination[1:]):
            trip_total += distances[f"{city1}-{city2}"]
        total_distances.add(trip_total)
    return total_distances

def part1(commands: str) -> int:
    """
    What is the distance of the shortest route?

    Get the minimal value from the set of trip total distances.
    """
    total = _get_all_trip_lengths(commands)
    return min(total)

def part2(commands: str) -> int:
    """
    What is the distance of the longest route?

    Get the maximal value from the set of trip total distances.
    """
    total = _get_all_trip_lengths(commands)
    return max(total)

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2015_9.txt")
    print(part1(instructions))
    print(part2(instructions))
