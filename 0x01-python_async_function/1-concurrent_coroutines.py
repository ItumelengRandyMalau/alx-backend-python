#!/usr/bin/env python3
"""
Spawn multiple wait_random coroutines and return a list of delays soreted.
"""
import asyncio
from typing import List
import importlib.util
import sys

# Dynamic import of the module with a name starting with a digit
module_name = '0-basic_async_syntax'
spec = importlib.util.spec_from_file_location(module_name, f'{module_name}.py')
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn multiple wait_random coroutines and return a list of delays in
    ascending order.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # List to hold individual wait_random coroutine tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather results of all tasks
    delays = await asyncio.gather(*tasks)

    # Return sorted delays
    return sorted(delays)
