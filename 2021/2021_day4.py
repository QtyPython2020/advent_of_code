# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _make_draw_and_boards(lines: tuple[str]) -> tuple[str, list[list[list[int]]]]:
    """

    """
    draw = [int(num) for num in lines[0].split(",")]
    boards = []
    board = []
    for line in lines[1:]:
        if len(line) == 0:
            board = []
            continue
        board.append([int(num) for num in re.findall(r"[0-9]{1,2}", line)])
        if len(board)==5:
            boards.append(board)
    return draw, boards

def _update_boards(set_boards: list[list[list[int]]],
                   draw: int) -> list[list[list[int]]]:
    """

    """
    for b_num, board in enumerate(set_boards):
        for row_num, row in enumerate(board):
            if draw not in row:
                continue
            for pos, field in enumerate(row):
                if field == draw:
                    set_boards[b_num][row_num][pos] = None
                    break
    return set_boards

def _check_board(set_boards: list[list[list[int]]]) -> list[list[int]]:
    """

    """
    for board in set_boards:
        # horizontal
        for row in board:
            if all(i is None for i in row):
                return board
        # vertical
        for col in range(len(board)):
            if all(i[col] is None for i in board):
                return board
    return

def _sum_unmarked_numbers(board: list[list[int]]) -> int:
    values = set(val for row in board for val in row if val is not None)
    return sum(values)

def part1(commands: tuple[str]):
    """
    What will your final score be if you choose that board?

    <>
    """
    numbers, boards = _make_draw_and_boards(commands)
    for number in numbers:
        boards = _update_boards(boards, number)
        winning_board = _check_board(boards)
        if winning_board:
            score = _sum_unmarked_numbers(winning_board) * number
            break
    return score

def part2(commands: tuple[str]):
    """
    Figure out which board will win last. Once it wins, what would its final score be?

    <>
    """
    numbers, boards = _make_draw_and_boards(commands)
    for number in numbers:
        boards = _update_boards(boards, number)
        while (winning_board:= _check_board(boards)) is not None:
            if len(boards) == 1:
                return _sum_unmarked_numbers(winning_board) * number
            boards = [b for b in boards if b != winning_board]

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2021_4.txt")
    print(part1(instructions))
    print(part2(instructions))
