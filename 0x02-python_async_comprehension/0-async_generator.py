#!/usr/bin/env python3
"""
Module that contains an async generator function.
This function yields random numbers asynchronously.
"""

import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields random numbers.

    This generator yields 10 random floating-point numbers
    between 0 and 10, with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
