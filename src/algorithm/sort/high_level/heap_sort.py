# pyright: strict
from calculate_time.calculate_time import calculate_time


def sift(data_set: list[int], low: int, high: int):
    """range the data to a proper heap (bigger up, smaller down)

    Time complexity:
        Worst situation: -
        Normal:O(log(n))

    Args:
        data_set (list[int]): the list to be sort
        low (int): the root of the stack
        high (int): the last element of the stack
    """
    i = low  # i first point to the root node
    j = (
        2 * i + 1
    )  # j is the bigger child node (first is the left child of the root node)
    tmp = data_set[low]  # store the data of the root node
    while j <= high:  # if the location of j is available
        if (
            j + 1 <= high and data_set[j + 1] > data_set[j]
        ):  # if the right child node exist and is bigger than left
            j = j + 1  # j switch to the right child node
        if data_set[j] > tmp:  # if the child node is bigger than the parent node
            data_set[i] = data_set[j]
            i = j  # to the below layer
            j = 2 * i + 1
        else:  # tmp is bigger
            data_set[i] = tmp  # put tmp value in a node
            break
    else:
        data_set[i] = tmp  # put tmp value in a leave


@calculate_time
def heap_sort(data_set: list[int]) -> list[int]:
    """sort int list (using heap)

    Time complexity:
        Worst situation: -
        Normal: O(n*log(n))

    Args:
        data_set (list[int]): the sorted list of integers

    Returns:
        list[int]: the sorted list of integers
    """
    # first : find the last non leave node
    n = len(data_set)
    # ((n-2)//2) -> the last child's parent
    for i in range((n - 2) // 2, -1, -1):
        sift(data_set, i, n - 1)
    # finish building heap

    # take elements out one by one
    for i in range(n - 1, -1, -1):
        # i point to the last element in the current heap
        data_set[0], data_set[i] = data_set[i], data_set[0]  # change the root to bottom
        sift(data_set, 0, i - 1)  # i-1 is the new high
    return data_set
