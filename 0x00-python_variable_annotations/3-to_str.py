#!/usr/bin/env python3

"""
Module: to_str

This module provides a simple function to convert a floating-point
number to its string representation.

Function:
    to_str(n): Returns the string representation of a floating-point number.

Example:
    >>> to_str(3.14)
    '3.14'
    >>> to_str(-0.5)
    '-0.5'
"""


def to_str(n: float) -> str:
    """
    Returns the string representation of a floating-point number.

    Args:
        n (float): The floating-point number to convert.

    Returns:
        str: The string representation of the input number.

    Example:
        >>> to_str(3.14)
        '3.14'
        >>> to_str(-0.5)
        '-0.5'
    """
    return str(n)
