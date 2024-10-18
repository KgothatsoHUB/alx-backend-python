#!/usr/bin/env python3
"""
Module to asynchronously collect float values from an async generator.
"""

import asyncio
from typing import List
from 0_async_generator import async_generator  

async def async_comprehension() -> List[float]:  # Proper return annotation
    """
    Asynchronously collects float values from an async generator.

    Returns:
        List[float]: A list of collected float values.
    """
    return [value async for value in async_generator()]  # Ensure float values are yielded

