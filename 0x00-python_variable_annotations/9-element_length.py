#!/usr/bin/env python3

"""
Module: element_length

This module provides a function to calculate the length of
each element in a list.

Function:
    element_length(lst): Returns a list of tuples containing
    each element and its length.

Example:
    >>> element_length(["hello", "world"])
    [('hello', 5), ('world', 5)]
    >>> element_length(["a", "abc", "abcd"])
    [('a', 1), ('abc', 3), ('abcd', 4)]
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples containing each element
    and its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, each
        containing a string and its length.

    Example:
        >>> element_length(["hello", "world"])
        [('hello', 5), ('world', 5)]
        >>> element_length(["a", "abc", "abcd"])
        [('a', 1), ('abc', 3), ('abcd', 4)]
    """
    return [(i, len(i)) for i in lst]
