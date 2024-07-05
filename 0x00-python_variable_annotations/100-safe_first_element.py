#!/usr/bin/env python3

"""
Module: safe_first_element

This module provides a function to safely retrieve the
first element of a sequence.
If the sequence is empty, the function returns None.

Function:
    safe_first_element(lst): Returns the first element
    of the sequence or None.

Example:
    >>> safe_first_element([1, 2, 3])
    1
    >>> safe_first_element([])
    None
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the sequence if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): The sequence to retrieve the
        first element from.

    Returns:
        Optional[Any]: The first element of the sequence,
        or None if the sequence is empty.

    Example:
        >>> safe_first_element([1, 2, 3])
        1
        >>> safe_first_element([])
        None
    """
    if lst:
        return lst[0]
    else:
        return None

