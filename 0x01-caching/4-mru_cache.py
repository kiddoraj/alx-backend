#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a MRU (Most Recently Used) caching system.
    """

    def __init__(self):
        """
        Initialize the class by calling the parent class's __init__ method.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Cache a key-value pair using MRU eviction strategy.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recently_used_key = self.usage.pop()
                del self.cache_data[most_recently_used_key]
                print("DISCARD: {}".format(most_recently_used_key))
            if key in self.usage:
                self.usage.remove(key)
            self.usage.append(key)
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
            return self.cache_data[key]
        return None
