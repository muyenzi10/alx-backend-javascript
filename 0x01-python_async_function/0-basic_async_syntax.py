#!/usr/bin/env python3
""" The basics of random  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronou  """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
