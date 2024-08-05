#!/usr/bin/env python3
""" Python asyncio to run multiple instances of an
asynchronous function concurrently"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times with the specified max_delay
    and returns the delays in ascending order

    Returns:
    list of all the delays (float values).
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    float_values = []
    for float_value in asyncio.as_completed(tasks):
        result = await float_value
        float_values.append(result)
    return sorted(float_values)
