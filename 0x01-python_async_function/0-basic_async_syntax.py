#!/usr/bin/env python3
"""The random libraries to execute
an asynchronous function"""

import asyncio
import random
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time.

    arguments:
    max_delay (int, optional): The max delay time in seconds.

    Returns:
    The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
