#!/usr/bin/env python3
"""Module script that solves the sum of a float nukbers."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Solves the sum of a list of float numbers.

    argument:
    input_list (List[float]): A list of float numbers.

    Returns:
    The sum as a float.
    """
    return sum(input_list)
