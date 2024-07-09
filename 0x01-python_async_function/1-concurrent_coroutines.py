#!/usr/bin/env python3

"""
This module provides asynchronous coroutines to wait for
random delays and to
spawn multiple wait_random coroutines.
"""

import asyncio
import importlib
from typing import List


module_name = "0_basic_async_syntax"
wait_random = importlib.import_module(module_name).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and
    returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = await asyncio.gather(*tasks)

    sorted_delays: List[float] = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
