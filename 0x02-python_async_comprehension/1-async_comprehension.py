#!/usr/bin/env python3
""" Contains async comprehension for
collecting random numbers."""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
    The 10 random numbers.
    """
    return [a async for a in async_generator()]
