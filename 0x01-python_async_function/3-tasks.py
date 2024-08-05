import asyncio
"""
create an asyncio.Task for the wait_random coroutine.
"""
from 0_basic_async_syntax import wait_random  # Adjust the import path as needed

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay value to pass to wait_random.

    Returns:
        asyncio.Task: A Task object that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
