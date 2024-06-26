#!/usr/bin/python3
""" LRU caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Caching System using LRU algorithm """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if not (key and item):
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
           not self.cache_data.get(key)):
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if not (key and self.cache_data.get(key)):
            return None

        key_value = self.cache_data.get(key)
        del self.cache_data[key]
        self.cache_data[key] = key_value

        return self.cache_data[key]
