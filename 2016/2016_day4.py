# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
from collections import Counter
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def _extract_elements(encrypted_name: str) -> tuple[str,int,str]:
    """

    """
    letters, numbers, check = re.findall(r"(.*)-(\d*)\[(\w*)\]",
                                         encrypted_name)[0]
    return letters.replace("-", ""), int(numbers), check

def _match_to_checksum(check_name: str, check_sum: str) -> bool:
    """

    """
    letter_counts = sorted(sorted(Counter(check_name).items(),
                                  key=lambda x:x[0],
                                  reverse=False),
                           key=lambda x:x[1],
                           reverse=True)
    test_str = "".join(x[0] for x in letter_counts)[:5]
    return test_str == check_sum

def _rotate_cipher(letter:str, times:int) -> str:
    """
    Apply the rotate cipher to the provided letter.
    """
    return chr((ord(letter)-97+times)%26+97)

def part1(commands: str) -> int:
    """
    What is the sum of the sector IDs of the real rooms?
    """
    sector_id_sum = 0
    for command in commands:
        name, sector_id, checksum = _extract_elements(command)
        if _match_to_checksum(name, checksum):
            sector_id_sum += sector_id
    return sector_id_sum

def part2(commands: str) -> int:
    """
    What is the sector ID of the room where North Pole objects are stored?
    """
    sector_id_sum = 0
    for command in commands:
        name, sector_id, checksum = _extract_elements(command)
        name = "".join(_rotate_cipher(letter, sector_id) for letter in name)
        checksum = "".join(_rotate_cipher(letter, sector_id) for letter in checksum)
        # if "north" not in name:
        #     continue
        if _match_to_checksum(name, checksum):
            sector_id_sum += sector_id
    return sector_id_sum

if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2016_4.txt")
    print(part1(instructions))
    print(part2(instructions))
