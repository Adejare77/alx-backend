#!/usr/bin/env python3
"""Hypermedia Pagination"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return range of indexes to return in a list of those
        particular pagination parameters"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        offset = (page - 1) * page_size
        current_page_size = offset + page_size

        dataset = self.dataset()
        result = []

        if current_page_size > len(dataset):
            current_page_size = len(dataset)

        if offset <= len(dataset):
            for i in range(offset, current_page_size):
                result.append(dataset[i])
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value paris
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_page: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        length_of_dataset = len(self.dataset())

        data_set = {
            'page_size': None,
            'page': page,
            'data': data,
            'next_page': None,
            'prev_page': None,
            'total_page': None
        }

        total_pages = math.ceil(length_of_dataset / page_size)

        data_set['page_size'] = len(data)

        if (page < total_pages):
            data_set['next_page'] = page + 1

        if (page > 1):
            data_set['prev_page'] = page - 1

        data_set['total_page'] = total_pages

        return data_set
