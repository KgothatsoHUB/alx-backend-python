#!/usr/bin/env python3
import asyncio
from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension."""
    return [number async for number in async_generator()]
