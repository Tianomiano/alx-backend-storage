#!/usr/bin/env python3
"""
Main file
"""

Cache = __import__('exercise').Cache

cache = Cache()

data = 'bar'
data1 = 123
key = cache.store(data)
key1 = cache.store(data1)

print(cache.get_str(key))
print(cache.get_int(key1))