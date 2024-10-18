#!/usr/bin/env python3
import asyncio
import time
from typing import List
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime of running async_comprehension four times in parallel."""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
