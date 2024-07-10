#!/usr/bin/env python3

"""
This module contains a coroutine that collects
10 random numbers using an async comprehension 
over async_generator and returns the collected
numbers.
"""

import asyncio
from typing import List

# Dynamically import the async_generator from 0-async_generator.py
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    using an async comprehension over async_generator
    and returns the collected numbers.

    Returns:
        list[float]: A list of 10 random floating-point
        numbers.
    """
    return [number async for number in async_generator()]
