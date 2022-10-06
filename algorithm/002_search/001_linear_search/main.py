# pyright: strict
"""linear search question"""


from typing import List, TypeVar

T = TypeVar("T")


def linear_search(data_set: List[T], target_value: T) -> int | None:
    """linear search

    Args:
        data_set (List[T]): the data_set to search
        target_value (T): the target value to search

    Returns:
        int | None: if the target value is in data set
            return the index of the target value else return None
    """
    for key, value in enumerate(data_set):
        if value == target_value:
            return key
    return None


data_set_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(linear_search(data_set_1, 5))


data_set_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(linear_search(data_set_2, "F"))
