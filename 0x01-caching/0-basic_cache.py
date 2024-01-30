#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs.
    """

    def __init__(self):
        """
        Initialize the class by calling the parent class's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair in the cache.

        Args:
            key: The key for the item.
            item: The value to be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is not found
            or if it is None.
        """
        return self.cache_data.get(key)
