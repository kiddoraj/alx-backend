#!/usr/bin/env python3
"""
Contains class with methods to create simple pagination from csv data
"""

import csv
from typing import List, Dict
from .0-simple_helper_function import index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: List[List[str]] = []

    def dataset(self) -> List[List[str]]:
        """
        Reads from csv file and returns the dataset.
        Returns:
            List[List[str]]: The dataset.
        """
        if not self.__dataset:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the value is a positive integer.
        Args:
            value (int): The value to be asserted.
        """
        assert isinstance(value, int) and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns a page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            List[List[str]]: The page of the dataset.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Returns a page of the dataset with pagination information.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            dict: Pagination information and data.
        """
        total_pages = (len(self.dataset()) - 1) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": min(page_size, len(data)),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
