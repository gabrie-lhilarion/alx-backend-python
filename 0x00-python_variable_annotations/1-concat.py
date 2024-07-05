#!/usr/bin/env python3


"""
Module: concat

This module provides a simple function to concatenate two strings.

Function:
    concat(str1, str2): Returns the concatenation of two strings.

Example:
    >>> concat("Hello, ", "world!")
    'Hello, world!'
    >>> concat("foo", "bar")
    'foobar'
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.

    Example:
        >>> concat("Hello, ", "world!")
        'Hello, world!'
    """
    return str1 + str2
