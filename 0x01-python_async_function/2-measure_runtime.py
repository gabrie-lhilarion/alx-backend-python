#!/usr/bin/env python3

"""
This module provides a function to measure the average
runtime of the wait_n coroutine.
"""

import asyncio
import time
import importlib


module_name = "0_basic_async_syntax"
wait_n = importlib.import_module(module_name).wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per task.

    Args:
        n (int): The number of tasks.
        max_delay (int): The maximum delay for each task in seconds.

    Returns:
        float: The average time per task.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
