#!/usr/bin/env python3

"""
Module: to_kv

This module provides a function to create a tuple from a
string and a number (integer or float).
The tuple contains the string and the square of the number.

Function:
    to_kv(k, v): Returns a tuple with the string and the
    square of the number.

Example:
    >>> to_kv("age", 3)
    ('age', 9.0)
    >>> to_kv("pi", 3.14)
    ('pi', 9.8596)
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number (integer or float) to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
                    and thesecond element is the square of `v` as a float.

    Example:
        >>> to_kv("age", 3)
        ('age', 9.0)
        >>> to_kv("pi", 3.14)
        ('pi', 9.8596)
    """
    return (k, float(v ** 2))
