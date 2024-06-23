#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary with the following key-value pairs

        Args:
        index(int): the current start index of the return page. That is
        the index of the first item in the current page. For example if
        requesting page 3 with page_size 20, and no data was removed from
        the dataset, the current index should be 60

        next_index(int): the next index to query with. That should be the
        index of the first item after the last item on the current page.

        page_size(int): the current page size

        data: the actual page of the dataset
        """
        data = self.dataset()
        assert index >= 0 and index < len(data)

        data_set = {
            'index': index,
            'next_index': None,
            'page_size': page_size,
            'data': None
        }

        next_index = index + page_size
        indexed_data_set = self.indexed_dataset()

        actual_data = []
        while (index < next_index and next_index < len(data)):
            if not indexed_data_set.get(index):
                next_index += 1
            else:
                actual_data.append(indexed_data_set.get(index))

            index += 1

        data_set['next_index'] = next_index
        data_set['data'] = actual_data

        return data_set
