#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class by calling the parent class's __init__ method.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair using FIFO eviction strategy.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                evicted_key = self.order.pop(0)
                del self.cache_data[evicted_key]
                print("DISCARD: {}".format(evicted_key))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key)
