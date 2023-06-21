# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import hashlib
from helpers.helper_functions import read_single_line_to_str

def part1(door_id: str) -> str:
    """
    Given the actual Door ID, what is the password?
    """
    count = 0
    password = ""
    for _ in range(8):
        while True:
            count += 1
            str2hash = f"{door_id}{count}"
            encoding = str2hash.encode()
            result = hashlib.md5(encoding)
            md5hash = result.hexdigest()
            if md5hash.startswith("00000"):
                password += md5hash[5]
                break
    return password

def part2(door_id: str):
    """
    Given the actual Door ID and this new method, what is the password?
    """
    count = 0
    password = ["."]*8
    for _ in range(8):
        while True:
            count += 1
            str2hash = f"{door_id}{count}"
            encoding = str2hash.encode()
            result = hashlib.md5(encoding)
            md5hash = result.hexdigest()
            if md5hash.startswith("00000"):
                print(md5hash)
                pos = int(md5hash[5])
                password[pos] = md5hash[6]
                break
    return password

if __name__ == "__main__":
    instructions = read_single_line_to_str("input_2016_5.txt")
    # print(part1(instructions))
    print(part2(instructions))
