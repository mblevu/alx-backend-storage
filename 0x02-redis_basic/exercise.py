#!/usr/bin/env python3
"""writing strings to redis"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """cache class"""
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int]) -> str:
        """generate random id using uuid and
        store data in redis using the random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
