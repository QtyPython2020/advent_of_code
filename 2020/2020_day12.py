# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re
from helpers.helper_functions import read_multiple_lines_to_tuple_of_str

def part1(commands: str):
    pos_x, pos_y = 0,0
    direction = (1,0)
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    switch = {"N": lambda d,v,x,y: (d,
                                    x+directions[0][0]*v,
                                    y+directions[0][1]*v),
              "E": lambda d,v,x,y: (d,
                                    x+directions[1][0]*v,
                                    y+directions[1][1]*v),
              "S": lambda d,v,x,y: (d,
                                    x+directions[2][0]*v,
                                    y+directions[2][1]*v),
              "W": lambda d,v,x,y: (d,
                                    x+directions[3][0]*v,
                                    y+directions[3][1]*v),
              "L": lambda d,v,x,y: (d:=directions[(directions.index(d)-v//90)%4],
                                    x,
                                    y),
              "R": lambda d,v,x,y: (d:=directions[(directions.index(d)+v//90)%4],
                                    x,
                                    y),
              "F": lambda d,v,x,y: (d,
                                    x+d[0]*v,
                                    y+d[1]*v)}
    for command in commands:
        action, value = re.findall("(\w)(\d*)", command)[0]
        direction, pos_x, pos_y = switch.get(action)(direction, int(value), pos_x, pos_y)
    return abs(pos_x) + abs(pos_y)

def part2(commands: str):
    pos_x, pos_y = 0,0
    waypoint_x, waypoint_y = 10,1
    direction = (1,0)
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    switch = {"N": lambda d,v,x,y,wx,wy: (d,
                                          x,
                                          y,
                                          wx+directions[0][0]*v,
                                          wy+directions[0][1]*v),
              "E": lambda d,v,x,y,wx,wy: (d,
                                          x,
                                          y,
                                          wx+directions[1][0]*v,
                                          wy+directions[1][1]*v),
              "S": lambda d,v,x,y,wx,wy: (d,
                                          x,
                                          y,
                                          wx+directions[2][0]*v,
                                          wy+directions[2][1]*v),
              "W": lambda d,v,x,y,wx,wy: (d,
                                          x,
                                          y,
                                          wx+directions[3][0]*v,
                                          wy+directions[3][1]*v),
              "L": lambda d,v,x,y,wx,wy: (d,
                                          x,
                                          y,
                                          *[(wy,-wx),(-wx,-wy),(wx,-wy)][(270-v)//90]),
              "R": lambda d,v,x,y,wx,wy: (d,
                                          x,
                                          y,
                                          *[(wy,-wx),(-wx,-wy),(wx,-wy)][(v-90)//90]),
              "F": lambda d,v,x,y,wx,wy: (d,
                                          x+wx*v,
                                          y+wy*v,
                                          wx,
                                          wy)}
    for command in commands:
        action, value = re.findall("(\w)(\d*)", command)[0]
        direction, pos_x, pos_y, waypoint_x, waypoint_y = switch.get(action)(direction, int(value), pos_x, pos_y, waypoint_x, waypoint_y)
        print(command, pos_x, pos_y, waypoint_x, waypoint_y)
    return abs(pos_x) + abs(pos_y)


if __name__ == "__main__":
    instructions = read_multiple_lines_to_tuple_of_str("input_2020_12.txt")
    print(part1(instructions))
    print(part2(instructions))
