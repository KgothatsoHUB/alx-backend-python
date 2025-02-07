#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """    Returns an asyncio.Task object for wait_random with the specified max_delay."""
    return asyncio.create_task(wait_random(max_delay))
