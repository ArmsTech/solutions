"""Celery tasks."""

import os
import time

import celery
import numpy

from median.persistence import redis_app

celery_app = celery.Celery()
celery_app.config_from_object('median.settings')


@celery_app.task(bind=True)
def get_median_for_last_min(task, from_time):
    """Get the median for the last minute from a specified time.

    Args:
        from_time (float): Request time in seconds since the epoch.

    Returns:
        int: The median for the last minute.
    """
    epoch_time = time.time()
    elements = redis_app.zrangebyscore(
        os.environ['MEDIAN_SET_KEY'],
        epoch_time - float(os.environ['MEDIAN_LAST_X_SECONDS']), epoch_time)
    # elements e.g. ['7d529dd4-548b-4258-aa8e-23e34dc8d43d:200', ...]
    integers = [int(element.split(':')[1]) for element in elements]

    # Don't give numpy an empty list
    return numpy.median(integers or 0)


@celery_app.task()
def remove_old_integers():
    """Remove integers that will not be included in median calculation."""
    epoch_time = time.time()
    removed = redis_app.zremrangebyscore(
        'integers', '-inf',
        epoch_time - float(os.environ['REMOVE_LAST_X_SECONDS']))
    print "{0} old elements removed from {1} set.".format(
        removed, os.environ['MEDIAN_SET_KEY'])
