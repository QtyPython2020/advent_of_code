# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

def read_single_line_to_str(path: str) -> str:
    """


    Parameters
    ----------
    path : str
        DESCRIPTION.

    Returns
    -------
    content : str
        DESCRIPTION.

    """
    with open(path, "r") as file:
        content = file.readline()
    return content

if __name__ == "__main__":
    pass
