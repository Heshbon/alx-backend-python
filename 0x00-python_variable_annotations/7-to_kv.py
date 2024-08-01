#!/usr/bin/env python3
"""Module script that converts a string and an int/float to a tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and an int/float to a tuple

    arguments:
    k (str): The first element of the tuple is the string.
    v (Union[int, float]): The second element is the square of the int/float.

    Returns:
    A tuple.
    """
    return (k, float(v ** 2))
