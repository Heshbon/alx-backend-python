#!/usr/bin/env python3
""" Script module that augment the correct duck-typed annotations."""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence, or None if the sequence is empty.

    Parameters:
    lst (Sequence[Any]): The sequence to return the first element

    Returns:
    The elements of the sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
