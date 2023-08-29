#!/usr/bin/env python3
"""Import Modules"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        funtion that have delay of 10 seconds and also
        print numbers aleatory
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
