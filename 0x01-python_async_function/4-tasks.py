#!/usr/bin/env python3

"""
This module provides a function to create multiple
asyncio.Tasks for the wait_random coroutine.
"""

import asyncio
from typing import List
import importlib

# Import task_wait_random from task_wait_random.py
task_wait_random = importlib.import_module("task_wait_random").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = await asyncio.gather(*tasks)
    sorted_delays: List[float] = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
