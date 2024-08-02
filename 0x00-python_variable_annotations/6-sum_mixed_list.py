#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats
        to be summed.

    Returns:
        float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
