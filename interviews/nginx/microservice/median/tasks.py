"""Celery tasks."""

import time

import celery
import numpy

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
    elements = redis_store.zrangebyscore(
        'integers', epoch_time - EPOCH_MINUTE, epoch_time)
    # elements e.g. ['7d529dd4-548b-4258-aa8e-23e34dc8d43d:200', ...]
    integers = [int(element.split(':')[1]) for element in elements]

    # Don't give numpy an empty list
    return numpy.median(integers or 0)
