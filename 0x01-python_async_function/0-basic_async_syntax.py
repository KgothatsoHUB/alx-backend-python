#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay (inclusive)and returns the actual delay as a float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
