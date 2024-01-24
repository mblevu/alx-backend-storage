#!/usr/bin/env python3
"""writing strings to redis"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


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
    
    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int]:
        """get data from redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get to str"""
        return self.get(key, str)
    
    def get_int(self, key: str) -> str:
        """automatically parametrize Cache.get to int"""
        return self.get(key, int)  
