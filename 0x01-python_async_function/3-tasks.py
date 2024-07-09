#!/usr/bin/env python3

"""
This module provides a function to create an asyncio.
Task for the wait_random coroutine.
"""

import asyncio
import importlib


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the
    wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    module_name = "0_basic_async_syntax"
    wait_random = importlib.import_module(module_name).wait_random
    return asyncio.create_task(wait_random(max_delay))
