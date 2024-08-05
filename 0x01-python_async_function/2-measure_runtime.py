#!/usr/bin/env python3
""" Measures the total execution time for wait_n(n, max_delay)
and returns total_time / n"""

import asyncio
import time
from typing import Callable

# Import wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Synchronously measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Returns:
    A float.
    """
    start_time = time.time()

    async def async_wrapper():
        await wait_n(n, max_delay)

    asyncio.run(async_wrapper())

    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
