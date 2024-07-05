#!/usr/bin/env python3

"""
Module: zoom_array

This module provides a function to zoom in on
elements of a tuple.
The function returns a list where each item
in the input tuple is repeated
a specified number of times.

Function:
    zoom_array(lst, factor): Returns a list with each item in the input tuple
                             repeated 'factor' times.

Example:
    >>> array = (12, 72, 91)
    >>> zoom_2x = zoom_array(array)
    >>> zoom_2x
    [12, 12, 72, 72, 91, 91]
    >>> zoom_3x = zoom_array(array, 3)
    >>> zoom_3x
    [12, 12, 12, 72, 72, 72, 91, 91, 91]
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list where each item in the input tuple is
    repeated 'factor' times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The multiplication
        factor. Defaults to 2.

    Returns:
        List[int]: A list with each item in the input
        tuple repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
