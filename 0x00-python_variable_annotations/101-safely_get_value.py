#!/usr/bin/env python3

"""
Module: safely_get_value

This module provides a function to safely retrieve a value from a dictionary.
If the key does not exist in the dictionary, the function returns a default value.

Function:
    safely_get_value(dct, key, default): Returns the value associated with the key or the default value.

Example:
    >>> my_dict = {'a': 1, 'b': 2}
    >>> safely_get_value(my_dict, 'a')
    1
    >>> safely_get_value(my_dict, 'c', 3)
    3
"""

from typing import TypeVar, Mapping, Any, Optional

# Define a TypeVar for the return value
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Optional[T] = None
        ) -> Optional[T]:
    """
    Returns the value associated with the given key
    in the dictionary.  If the key does not exist,
    returns the default value.

    Args:
        dct (Mapping[Any, T]): The dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Optional[T], optional): The default value 
        to return if the key is not found. Defaults to None.

    Returns:
        Optional[T]: The value associated with the key, 
        or the default value.

    Example:
        >>> my_dict = {'a': 1, 'b': 2}
        >>> safely_get_value(my_dict, 'a')
        1
        >>> safely_get_value(my_dict, 'c', 3)
        3
    """
    if key in dct:
        return dct[key]
    else:
        return default
