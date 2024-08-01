#!/usr/bin/env python3
"""Returns the value for a given key from a dictionary."""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value for a given key from a dictionary.

    Parameters:
    dct (Mapping): The dictionary value.
    key (Any): The key in the dictionary
    default (Union[T, None], optional): The default value to return.

    Returns:
    The return values, add type annotations to the function.
    """
    if key in dct:
        return dct[key]
    else:
        return default
