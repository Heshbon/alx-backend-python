#!/usr/bin/env python3
"""Module that create asyncio tasks that
wait_random coroutine"""

import asyncio
from typing import Callable

# Import wait_random from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a asyncio tasks for the wait_random coroutine

    Returns:
    Asyncio.Task.
    """
    # Schedule the execution of wait_random
    task = asyncio.create_task(wait_random(max_delay))
    return task
