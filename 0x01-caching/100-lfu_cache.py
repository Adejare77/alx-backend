#!/usr/bin/python3
""" LFU caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Caching System using LFU algorithm """

    def __init__(self):
        super().__init__()
        self.key_freq = {}
        self.key_index = -1

    def put(self, key, item):
        """ Add an item in the cache """
        if not (key and item):
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
           not self.cache_data.get(key)):
            # list all frequencies values
            all_keys_list = list(self.key_freq.values())
            # find the least frequency value (always the first min value)
            min_freq = min(all_keys_list)
            # finds the index of the min frequency value
            self.key_index = all_keys_list.index(min_freq)
            # finds it's corresponding key `name`
            corr_index_key = list(self.key_freq.keys())[self.key_index]
            # Delete from cache_data and key_freq
            del self.cache_data[corr_index_key]
            del self.key_freq[corr_index_key]
            print(f"DISCARD: {corr_index_key}")

        self.cache_data[key] = item
        # add 1 to key frequency value, if not present, then 1
        freq_value = self.key_freq.get(key, 0) + 1
        # purpose of below is to always move last called key to last in cache
        if key in self.key_freq.keys():
            del self.key_freq[key]
        # After deleting, re-add. Thus moves to the last item in cache
        self.key_freq[key] = freq_value

    def get(self, key):
        """ Get an item by key """
        if not (key and self.cache_data.get(key)):
            return None

        # add 1 to key frequency for every called key
        freq_value = self.key_freq.get(key, 0) + 1
        # purpose of below is to always move last called key to last in cache
        del self.key_freq[key]
        # After deleting, re-add. Thus moves to the last item in cache
        self.key_freq[key] = freq_value

        return self.cache_data[key]
