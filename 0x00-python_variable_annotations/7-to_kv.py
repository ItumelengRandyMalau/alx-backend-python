#!/usr/bin/env python3
"""
This module provides a function to convert a string and an int/float to a
tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string and an int/float to a tuple.

    Args:
        k (str): The string element.
        v (Union[int, float]): The int or float element.

    Returns:
        Tuple[str,float]:A tuple containing k and the square of v (as a float).
    """
    return k, v ** 2.0
