# pyright: strict
"""sorting algorithm"""
from typing import List
from calculate_time.calculate_time import calculate_time


@calculate_time
def bubble_sort(data_set: List[int]) -> List[int]:
    """bubble_sort

    Info:
        Time complexity:
            Best situation(sorted): O(n)
            Worst situation: O(n^2)
        loop through the data set,
        switch the bigger one to the front

    Args:
        data_set (List[int]): the data set to sort

    Returns:
        List[int]: the sorted result
    """
    for i in range(len(data_set) - 1):
        exchange = False  # when no change at a round, finish the sorting
        for j in range(len(data_set) - i - 1):
            if data_set[j + 1] < data_set[j]:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]
                exchange = True
        if not exchange:
            return data_set
    return data_set


@calculate_time
def select_sort(data_set: List[int]) -> List[int]:
    """select_sort

    Info:
        Time complexity:
            Best situation(sorted): O(n^2)
            Worst situation: O(n^2)
        loop through the data set,
        every round get min_value and switch to the first item which is unsorted

    Args:
        data_set (List[int]):  the data set to sort

    Returns:
        List[int]: the sorted result
    """
    for i in range(len(data_set) - 1):  # i is the count of round
        min_value_index = i
        for j in range(i + 1, len(data_set)):
            if data_set[min_value_index] > data_set[j]:
                min_value_index = j
        data_set[min_value_index], data_set[i] = (
            data_set[i],
            data_set[min_value_index],
        )

    return data_set


@calculate_time
def insert_sort(data_set: List[int]) -> List[int]:
    """insert_sort

    Info:
        Time complexity:
            Best situation(sorted): O(n)
            Worst situation: O(n^2)
        loop through the data set,
        every round get min_value and switch to the first item which is unsorted

    Args:
        data_set (List[int]):  the data set to sort

    Returns:
        List[int]: the sorted result
    """
    for i in range(1, len(data_set)):  # the index of new select
        tmp = data_set[i]
        j = i - 1  # the index of sorted
        while j >= 0 and data_set[j] > tmp:  # linear search
            data_set[j + 1] = data_set[j]
            j -= 1
        data_set[j + 1] = tmp
    return data_set


@calculate_time
def insert_sort_binary_search(data_set: List[int]) -> List[int]:
    """insert_sort_binary_search

    Info:
        Time complexity:
            Best situation(sorted): O(n)
            Worst situation: O(n^2)
        loop through the data set,
        every round get min_value and switch to the first item which is unsorted

    Args:
        data_set (List[int]):  the data set to sort

    Returns:
        List[int]: the sorted result
    """
    for i in range(1, len(data_set)):  # the index of new select
        tmp = data_set[i]
        j = i - 1  # the index of sorted
        data_set = binary_search_insert(data_set, j, tmp)
        # while j >= 0 and data_set[j] > tmp:  # linear search
        #    data_set[j + 1] = data_set[j]
        #    j -= 1
        # data_set[j + 1] = tmp
    print(data_set)
    return data_set


def binary_search_insert(data_set: List[int], j: int, target_value: int) -> List[int]:
    """binary_search

    Args:
        data_set (List[T]): the data_set to search
        target_value (T): the target value to search


    Returns:
        int | None: if the target value is in data set
            return the index of the target value else return None

    """

    if j == 0:
        return data_set
    elif j == 1:
        if target_value > data_set[0]:
            return data_set
        else:
            data_set[0], data_set[1] = data_set[1], data_set[0]
            return data_set
    left = 0
    right = j - 1
    mid = (left + right) // 2
    print(data_set)
    print(left, right)
    while left <= right:  # there is item in the candidate area
        if data_set[mid] == target_value:
            data_set.pop(j)
            data_set.insert(mid, target_value)
            return data_set
        elif data_set[mid] > target_value:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    data_set.pop(j)
    data_set.insert(mid + 1, target_value)
    return data_set
