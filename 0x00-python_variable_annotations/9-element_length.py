#!/usr/bin/env python3
"""
This module provides a function to return a list of tuples with elements
and their corresponding lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples, where each tuple contains an element from
    lst and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g.,
        strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        an element from lst and its length.
    """
    return [(i, len(i)) for i in lst]
