#!/usr/bin/env python3
"""Module script that sums a mixed list of inetergers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats.

    arguments:
    mxd_lst (List[Union[int, float]]):
    Contains both integers and floats.

    Returns:
    The sum as a float.
    """
    return sum(mxd_lst)
