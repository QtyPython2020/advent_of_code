import sys
sys.path.append("../helpers")
from helper_functions import read_single_line_to_str

def part1(commands):
    floor = 0
    up = commands.count("(")
    down = commands.count(")")
    return floor + up - down

def part2():
    floor = 0
    pass


instructions = read_single_line_to_str("input_2015_1.txt")
print(part1(instructions))
