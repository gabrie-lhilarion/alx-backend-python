#!/usr/bin/env python3

"""
Module: sum_mixed_list

This module provides a function to sum a list containing both
integers and floating-point numbers.

Function:
    sum_mixed_list(mxd_lst): Returns the sum of a list of integers and floats.

Example:
    >>> sum_mixed_list([1, 2.5, 3, 4.5])
    11.0
    >>> sum_mixed_list([0, -1.5, 2, 3.5])
    4.0
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers
    and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and
        floating-point numbers to sum.

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_mixed_list([1, 2.5, 3, 4.5])
        11.0
        >>> sum_mixed_list([0, -1.5, 2, 3.5])
        4.0
    """
    return sum(mxd_lst)
