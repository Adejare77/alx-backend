#!/usr/bin/env python3
"""Simple Pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and an
    end index corresponding to the range of indexes to return in
    a list of those particular pagination parameters
    """
    offset = (page - 1) * page_size
    current_page_size = offset + page_size
    return (offset, current_page_size)


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
