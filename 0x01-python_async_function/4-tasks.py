#!/usr/bin/env python3

""" Module that create asyncio tasks that
wait_random coroutine"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `n` tasks with random delays up to `max_delay` and
    returns sorted results.


    Returns:
    Float values in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    float_values = await asyncio.gather(*tasks)
    return sorted(float_values)
