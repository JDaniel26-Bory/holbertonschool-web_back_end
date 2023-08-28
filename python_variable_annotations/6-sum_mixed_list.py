#!/usr/bin/env python3
"""Import Modules"""
from typing import List, Union
""" function sum_mixed_list which takes a list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns their sum as a float."""
    return sum(mxd_lst)
