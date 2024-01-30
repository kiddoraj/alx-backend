#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU (Least Frequently Used) caching system.
    """

    def __init__(self):
        """
        Initialize the class by calling the parent class's __init__ method.
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Cache a key-value pair using LFU eviction strategy.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                least_used_key = min(self.usage.index(k) for k in lfu_keys)
                least_used_key = self.usage[least_used_key]
                print("DISCARD: {}".format(least_used_key))
                del self.cache_data[least_used_key]
                del self.frequency[least_used_key]
                self.usage.remove(least_used_key)
            if key in self.usage:
                self.usage.remove(key)
            self.usage.append(key)
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
