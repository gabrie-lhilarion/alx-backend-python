#!/usr/bin/env python3

"""
Module: add

This module provides a simple function to add two floating-point numbers.

Function:
    add(a, b): Returns the sum of two floating-point numbers.

Example:
    >>> add(1.5, 2.5)
    4.0
    >>> add(-1.0, 3.0)
    2.0
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.

    Example:
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b
