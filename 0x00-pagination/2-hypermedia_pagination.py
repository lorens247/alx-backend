#!/usr/bin/env python3

"""
Simple pagination class and the helper functions
to practice cursor based API pagination
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end indices for paginating a dataset.

    Args:
        page (int): The current page number (1-based).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Retrieve a specific page of data from the dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page
                                        Defaults to 10

        Returns:
            List[List]: A list containing the data for the specified page.

        Raises:
            AssertionError: If the input parameters are not valid
            (e.g., non-integer values or non-positive page/page_size).
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        Get information about a specific page within a paginated dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page.
                                        Defaults to 10.

        Returns:
            Dict: A dictionary containing information about the specified page,
            including:
                - 'page_size': The number of items on the current page.
                - 'page': The current page number.
                - 'data': The data for the current page.
                - 'next_page': The next page num or None if it's the last page
                - 'prev_page': The previous page number or None if first page.
                - 'total_pages': The total number of pages in the dataset.
        '''
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info