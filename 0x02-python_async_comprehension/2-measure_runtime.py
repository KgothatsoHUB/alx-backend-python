import asyncio
import time

# Dynamically import the module with a name starting with a number
module = __import__('1-async_comprehension')
async_comprehension = getattr(module, '1-async_comprehension')

async def measure_runtime() -> float:
    """Measures the total runtime for executing async_comprehension 4 times in parallel."""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
