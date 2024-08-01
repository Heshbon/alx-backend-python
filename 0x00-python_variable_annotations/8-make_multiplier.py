#!/usr/bin/env python3
""" Script module that takes a float multiplier as argument."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    The multiplier function.

    argument:
    multiplier (float): The multiplier value for the returned function.

    Returns:
    A function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
