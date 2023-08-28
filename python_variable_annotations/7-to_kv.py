#!/usr/bin/env python3
"""Impor modules"""
from typing import Tuple, Union
"""Function that return a tuple with its data"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple"""
    squared_value = v * v
    return k, squared_value
