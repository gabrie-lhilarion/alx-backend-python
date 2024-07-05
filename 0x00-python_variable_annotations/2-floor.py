#!/usr/bin/env python3


"""
Module: floor

This module provides a simple function to calculate the
floor of a floating-point number.

Function:
    floor(n): Returns the floor of a floating-point number.

Example:
    >>> floor(3.7)
    3
    >>> floor(-2.3)
    -3
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The floor of the input number.

    Example:
        >>> floor(3.7)
        3
        >>> floor(-2.3)
        -3
    """
    return math.floor(n)
