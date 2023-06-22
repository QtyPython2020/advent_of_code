# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

class Reindeer:
    """
    A class for the reindeer that contains a state whether it is flying or resting.
    Furthermore, all the specific details for coming to the distance covered are stored.
    Finally, two methods are in place: one for calculating the distance covered and one
    for awarding points.
    """
    def __init__(self, name:str, speed:str, duration:str, rest:str):
        self.name = name
        self.speed = int(speed)
        self.duration = int(duration)
        self.rest = int(rest)
        self.distance = 0
        self.state = "fly"
        self.time = self.duration
        self.points = 0

    def tick(self):
        """
        Determine the state of the reindeer at that moment and the resulting distance
        """
        if self.state == "fly":
            if self.time > 0:
                self.time -= 1
                self.distance += self.speed
            else:
                self.state = "rest"
                self.time = self.rest - 1
        elif self.state == "rest":
            if self.time > 0:
                self.time -= 1
            else:
                self.state = "fly"
                self.distance += self.speed
                self.time = self.duration - 1

    def get_point(self):
        """
        Add a point for the reindeer
        """
        self.points += 1


def _get_description(line: str)-> tuple[str]:
    """
    Extract the first word and all numeric values.
    """
    details = re.findall(r"(\w*)\s\D*(\d*)\D*(\d*)\D*(\d*)", line)[0]
    return details

def part1(commands: str, time: int) -> int:
    """
    After exactly 2503 seconds, what distance has the winning reindeer traveled?

    For each reindeer make an object based on the provided description. Then go through
    the seconds to get the total distance for each reindeer and return the maximum value.
    """
    reindeers = []
    for command in commands:
        name, speed, duration, rest = _get_description(command)
        reindeers.append(Reindeer(name, int(speed), int(duration), int(rest)))
    for _ in range(time):
        [reindeer.tick() for reindeer in reindeers]
    return max({reindeer.distance for reindeer in reindeers})

def part2(commands: str, time: int) -> int:
    """
    After exactly 2503 seconds, how many points does the winning reindeer have?

    For each reindeer make an object based on the provided description. Then go through
    the seconds to get the total distance for each reindeer and return the maximum value.
    """
    reindeers = []
    for command in commands:
        name, speed, duration, rest = _get_description(command)
        reindeers.append(Reindeer(name, int(speed), int(duration), int(rest)))
    for _ in range(time):
        [reindeer.tick() for reindeer in reindeers]
        dists = sorted([(reindeer, reindeer.distance) for reindeer in reindeers],
                       key=lambda x: x[1],
                       reverse=True)
        # find the furthests distance at that moment
        lead = max(dist for _,dist in dists)
        # award a point to each reindeer that is in the lead
        [reindeer.get_point() for reindeer in reindeers if reindeer.distance == lead]
    return max(reindeer.points for reindeer in reindeers)

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2015_14.txt")
    print(part1(instructions, 2503))
    print(part2(instructions, 2503))
