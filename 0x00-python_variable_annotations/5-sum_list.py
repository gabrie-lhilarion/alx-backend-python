#!/usr/bin/env python3

"""
Module: sum_list

This module provides a function to sum a list of
floating-point numbers.

Function:
    sum_list(input_list): Returns the sum of a list of floats.

Example:
    >>> sum_list([1.0, 2.5, 3.14])
    6.64
    >>> sum_list([0.0, -1.0, 1.0])
    0.0
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_list([1.0, 2.5, 3.14])
        6.64
        >>> sum_list([0.0, -1.0, 1.0])
        0.0
    """
    return sum(input_list)
