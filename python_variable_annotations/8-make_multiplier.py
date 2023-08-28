#!/usr/bin/env python3
"""Import Modules"""
from typing import Callable
""" function make_multiplier returns a function that multiplies a float."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by a given multiplier.
    """
    def multiplier_fun(n: float) -> float:
        """Return all multiplies"""
        return n * multiplier
    return multiplier_fun
