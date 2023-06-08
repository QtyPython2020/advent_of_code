# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

def read_single_line_to_str(path):
    with open(path, "r") as file:
        content = file.readline()
    return content

if __name__ == "__main__":
    pass
