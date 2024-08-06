#!/usr/bin/env python3

""" This module contains a coroutine named async_comprehension
that takes no arguments.
Coroutine will collect 10 random numbers using an async comprehensing over
async_generator, then return the 10 random numbers.
"""

import asyncio
from random import uniform
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that collects 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    return [num async for num in async_generator()]
