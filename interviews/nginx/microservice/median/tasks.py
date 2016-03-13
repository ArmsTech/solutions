"""Celery tasks."""

import time

import celery

from median.persistence import redis_store

# Seconds
EPOCH_MINUTE = 60

median_celery = celery.Celery()


@median_celery.task
def get_median_for_last_min(from_time):
    """Get the median for the last minute from a specified time.

    Args:
        from_time (float): Request time in seconds since the epoch.

    Returns:
        int: The median for the last minute.
    """
    epoch_time = time.time()
    integers = redis_store.zrangebyscore(
        'integers', epoch_time - EPOCH_MINUTE, epoch_time)
    print str(integers)
