# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _get_seat_id(ticket_code: str) -> int:
    """
    Parse every letter of the ticket getting the lower half of the range for F and L,
    and the upper half for B and R. Finally, calculate the ID by taken 8 times the row
    plus the seat.
    """
    options = {"F": lambda x,y: (_get_lowerhalf(x), y),
               "B": lambda x,y: (_get_upperhalf(x), y),
               "L": lambda x,y: (x, _get_lowerhalf(y)),
               "R": lambda x,y: (x, _get_upperhalf(y))}
    row = list(range(128))
    seat = list(range(8))
    for char in ticket_code:
        row, seat = options[char](row, seat)
    seat_id = row[0]*8+seat[0]
    return seat_id

def _get_lowerhalf(values: list) -> list:
    """
    Return a list that is the lower half of the given range by start at the lowest value and
    going up to maximum value minus half the range.
    """
    return list(range(min(values), max(values)-(max(values)-min(values))//2))

def _get_upperhalf(values: list) -> list:
    """
    Return a list that is the lower half of the given range by start at the lowest value plus half
    the range and one and going up to the maximum plus one for the range function.
    """
    return list(range(min(values)+(max(values)-min(values))//2+1, max(values)+1))

def part1(tickets: tuple[str]):
    """
    What is the highest seat ID on a boarding pass?

    Find the highest number from all the seat IDs.
    """
    highest_seat = 0
    for ticket in tickets:
        highest_seat = max(highest_seat, _get_seat_id(ticket))
    return highest_seat

def part2(tickets: tuple[str]):
    """
    What is the ID of your seat?

    Get all the seats that are on tickets and find the one that is missing in between that range.
    """
    seats = [_get_seat_id(ticket) for ticket in tickets]
    missing_ticket = [s for s in range(min(seats), max(seats)) if s not in seats][0]
    return missing_ticket

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2020_5.txt")
    print(part1(instructions))
    print(part2(instructions))
