#!/usr/bin/ env python3
"""
 Measure the average runtime of the wait_n coroutine.
"""
import asyncio
from time import time
from random import uniform
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather.
    Coroutine will measure the total runtime and return it.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start_time
