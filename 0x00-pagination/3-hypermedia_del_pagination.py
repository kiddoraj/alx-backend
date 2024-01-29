#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination information and data starting from the given index.

        Args:
            index (int): The index of the first item in the current page.
            page_size (int): The number of records per page.

        Returns:
            Dict: A dictionary containing the following key-value pairs:
                - index: The index of the first item in the current page.
                - next_index: The index of the first item in the next page if it exists, otherwise None.
                - page_size: The number of records in the current page.
                - data: The actual page of the dataset.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length

        response = {"index": index}
        data = []
        for _ in range(page_size):
            while index < data_length:
                curr = dataset.get(index)
                index += 1
                if curr:
                    data.append(curr)
                    break

        response["data"] = data
        response["page_size"] = len(data)
        response["next_index"] = index if index < data_length else None

        return response
