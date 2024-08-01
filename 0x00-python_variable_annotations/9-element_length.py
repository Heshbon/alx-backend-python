#!/usr/bin/env python3
"""Script module that returns a list of modules."""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples.

    parameters:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    Values with the appropriate types.
    """
    return [(i, len(i)) for i in lst]
