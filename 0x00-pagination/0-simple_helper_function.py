#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and an
    end index corresponding to the range of indexes to return in
    a list of those particular pagination parameters
    """
    offset = (page - 1) * page_size
    current_page_size = offset + page_size
    return (offset, current_page_size)
