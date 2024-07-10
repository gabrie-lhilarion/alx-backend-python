#!/usr/bin/env python3

"""
This module contains an asynchronous generator
that yields random numbers between 0 and 10
at 1-second intervals.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, each time asynchronously
    waits 1 second, and then yields a random floating-point
    number between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
