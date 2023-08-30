#!/usr/bin/env python3
"""Async basics"""
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Function that return a task"""
    t = create_task(wait_random(max_delay))
    return t