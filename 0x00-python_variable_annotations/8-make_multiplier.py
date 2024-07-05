#!/usr/bin/env python3

"""
Module: make_multiplier

This module provides a function to create a multiplier function.

Function:
    make_multiplier(multiplier): Returns a function that
    multiplies a float by the given multiplier.

Example:
    >>> multiplier_2 = make_multiplier(2.0)
    >>> multiplier_2(3.0)
    6.0
    >>> multiplier_2(4.5)
    9.0
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.

    Example:
        >>> multiplier_2 = make_multiplier(2.0)
        >>> multiplier_2(3.0)
        6.0
        >>> multiplier_2(4.5)
        9.0
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
