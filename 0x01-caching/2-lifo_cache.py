#!/usr/bin/python3
""" LIFO caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Caching System using LIFO algorithm """

    def __init__(self):
        super().__init__()
        self.key_index = -1

    def put(self, key, item):
        """ Add an item in the cache """
        if not (key and item):
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
            not self.cache_data.get(key)):
            last_item = list(self.cache_data.keys())[self.key_index]
            del self.cache_data[last_item]
            print(f"DISCARD: {last_item}")

        self.cache_data[key] = item
        self.key_index = list(self.cache_data.keys()).index(key)

    def get(self, key):
        """ Get an item by key """
        if not (key and self.cache_data.get(key)):
            return None
        return self.cache_data[key]
