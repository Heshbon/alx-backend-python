#!/usr/bin/env python3
""" Validates the pieces of code provided"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Repeats the element tuple.

    Parameters:
    - lst: Tuple of integers.
    - factor: Repetition factor.

    Returns:
    Repeated elements
    """
    return [item for item in lst for _ in range(factor)]


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
