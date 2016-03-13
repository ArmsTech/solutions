"""Manage persistence of integers for the median API."""

import redis

INTEGERS_SET_KEY = 'integers'

redis_store = redis.StrictRedis()
