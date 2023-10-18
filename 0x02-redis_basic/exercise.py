#!/usr/bin/env python3
"""Writing strings to Redis"""
import uuid
from functools import wraps
from typing import Callable, Optional, Union

import redis

def count_calls(method: Callable) -> Callable:
    """
    decorates a method to count how many times it was called
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    """
    A Cache class that writes to redis
    """

    def __init__(self) -> None:
        """
        store an instance of the Redis client,
        as a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random key using uuid,
        stores the input data in Redis using,
        the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None,
    ) -> Union[str, bytes, int, float, None]:
        """
        a get method that take a key string argument,
        and an optional Callable argument named fn
        """
        value = self._redis.get(key)
        if value is None:
                return None
        if fn is not None:
            return fn(value)
        return value

    def get_int(self, key: str) -> Union[int, None]:
        """
        parametrize Cache.get with the correct conversion function.
        return the value stored as an int
        """
        return self.get(key, int)

    def get_str(self, key: str) -> Union[str, None]:
        """
        parametrize Cache.get with the correct conversion function.
        returns the value stored as str
        """
        return self.get(key, str)