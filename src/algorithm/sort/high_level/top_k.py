"""to solve top k problem using heap sort"""
import random


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
            j + 1 <= high and data_set[j + 1] < data_set[j]
        ):  # if the right child node exist and is bigger than left
            j = j + 1  # j switch to the right child node
        if data_set[j] < tmp:  # if the child node is bigger than the parent node
            data_set[i] = data_set[j]
            i = j  # to the below layer
            j = 2 * i + 1
        else:  # tmp is bigger
            data_set[i] = tmp  # put tmp value in a node
            break
    else:
        data_set[i] = tmp  # put tmp value in a leave


def top_k(data_set: list[int], k: int) -> list[int]:
    """get the top k high number

    Args:
        data_set (list[int]): data set to get number
        k (int): the number need to output

    Returns:
        list[int]: output value
    """
    # 1. build heap
    heap = data_set[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)

    # 2. loop through
    for i in range(k, len(data_set) - 1):
        if data_set[i] > heap[0]:
            heap[0] = data_set[i]
            sift(heap, 0, k - 1)

    # 3. output
    for i in range(k - 1, -1, -1):
        # i point to the last element in the current heap
        heap[0], heap[i] = heap[i], heap[0]  # change the root to bottom
        sift(heap, 0, i - 1)  # i-1 is the new high
    return heap


datas = list(range(1000))
random.shuffle(datas)
print(top_k(datas, 10))
