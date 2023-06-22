# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _parse_claims(line: str) -> tuple[str, int, int, int, int]:
    """
    Extract all the numeric parts from the provided line.
    """
    claim_id, *others = re.findall(r"#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)",
                                   line)[0]
    pos_x, pos_y, width, height = (int(num) for num in others)
    return claim_id, pos_x, pos_y, width, height

def part1(claims: tuple[str]) -> int:
    """
    How many square inches of fabric are within two or more claims?

    Go through all the claims, count every time a square is claimed and return a
    total of all squares claimed more than once.
    """
    # this constructor makes a grid of zeroes that are not copies of eachother.
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        _, offset_x, offset_y, width, height = _parse_claims(claim)
        # increase every cell with one if it is in the claim
        for step_h in range(offset_y, offset_y + height):
            for step_w in range(offset_x, offset_x + width):
                grid[step_h][step_w] += 1
    multiple_claims = sum(sum(1 for cell in row if cell > 1) for row in grid)
    return multiple_claims

def part2(claims: tuple[str]):
    """
    What is the ID of the only claim that doesn't overlap?

    Go through all the claims and note down all claim IDs. When there is an overlap
    note these claims down and return the claim ID that is not in list of overlapping
    claims.
    """
    # this constructor makes a grid of zeroes that are not copies of eachother.
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    overlapping_claims = set()
    claim_ids = set()
    for claim in claims:
        claim_id, offset_x, offset_y, width, height = _parse_claims(claim)
        claim_ids.add(claim_id)
        # increase every cell with one if it is in the claim
        for step_h in range(offset_y, offset_y + height):
            for step_w in range(offset_x, offset_x + width):
                # when there is an overlap note down the claims
                if grid[step_h][step_w] != 0:
                    overlapping_claims.add(grid[step_h][step_w])
                    overlapping_claims.add(claim_id)
                grid[step_h][step_w] = claim_id
    not_overlapping_claim = claim_ids.difference(overlapping_claims)
    return not_overlapping_claim

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2018_3.txt")
    print(part1(instructions))
    print(part2(instructions))
