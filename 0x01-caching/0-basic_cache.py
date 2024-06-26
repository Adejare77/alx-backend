#!/usr/bin/python3
""" Basic Dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Caching system. This system has no limit """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if not (key and item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if not (key and self.cache_data.get(key)):
            return None
        return self.cache_data[key]
