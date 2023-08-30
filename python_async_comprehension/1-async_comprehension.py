#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension"""
    randon_numbers = [randon_num async for randon_num in async_generator()]
    return randon_numbers