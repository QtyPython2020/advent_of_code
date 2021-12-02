def part_1(puzzle_input):
    commands = puzzle_input
    horizon, depth = 0, 0
    for command in commands:
        if command.startswith("forward"):
            horizon += int(command[-1])
        elif command.startswith("down"):
            depth += int(command[-1])
        elif command.startswith("up"):
            depth -= int(command[-1])        
    return horizon * depth
    

def part_2(puzzle_input):
    commands = puzzle_input
    horizon, depth, aim = 0, 0, 0
    for command in commands:
        if command.startswith("forward"):
            horizon += int(command[-1])
            depth += aim * int(command[-1])
        elif command.startswith("down"):
            aim += int(command[-1])
        elif command.startswith("up"):
            aim -= int(command[-1])        
    return horizon * depth

with open("input_2021_day2.txt") as file:
    puzzle_input = [line.rstrip("\n")for line in file]
    
print(part_1(puzzle_input))
print(part_2(puzzle_input))