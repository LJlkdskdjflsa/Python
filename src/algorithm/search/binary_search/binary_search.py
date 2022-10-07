# pyright: strict
"""binary search question"""
from typing import List
from calculate_time.calculate_time import calculate_time


@calculate_time
def binary_search(data_set: List[int], target_value: int) -> int | None:
    """binary_search

    Args:
        data_set (List[T]): the data_set to search
        target_value (T): the target value to search


    Returns:
        int | None: if the target value is in data set
            return the index of the target value else return None

    """
    left = 0
    right = len(data_set) - 1
    while left <= right:  # there is item in the candidate area
        mid = (left + right) // 2
        if data_set[mid] == target_value:
            return mid
        elif data_set[mid] > target_value:
            right = mid - 1
        else:
            left = mid + 1
    return None


# data_set_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(binary_search(data_set_1, 5))
