#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page number and page size
    in a pagination system.

    Args:
        page (int): The page number to return (pages are 1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices for the
        requested page.
    """
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
