"""merge sort
sort number list
- recurrent saperate list to two
- until the list contians only one element(stop situation: one element is sorted)
- merge list
"""

import random


def merge(data_set: list[int], low: int, mid: int, high: int):
    """merge two sorted lists

    Time complexity of merge:
        1 merge: n

    Args:
        data_set (list[int]): data need to merge 
        low (int): the first element of the left list
        mid (int): the last element of the left list
        high (int): the first element of the right list
    """    
    left = low
    right = mid + 1
    data_tmp: list[int] = []
    while left <= mid and right <= high:
        if data_set[left] <= data_set[right]:
            data_tmp.append(data_set[left])
            left += 1
        else:
            data_tmp.append(data_set[right])
            right += 1

    while left <= mid:
        data_tmp.append(data_set[left])
        left += 1

    while right <= high:
        data_tmp.append(data_set[right])
        right += 1

    data_set[low : high + 1] = data_tmp


def merge_sort(data_set: list[int], low: int = 0, high: int = 0):
    """merge sort

    Time complexity:
        1 merge: n
        need to merge log(n) layer
        Time complexity = O(n*log(n))
    Space Complexity:
        O(n)
    Args:
        data_set (list[int]): data need to sort 
        low (int, optional): the lower bound of the list need to be sorted. Defaults to 0.
        high (int, optional):the upper bound of the list need to be sorted. Defaults to 0.
    """    
    if high == 0:
        high = len(data_set) - 1
    if low < high:  # at least two elements
        mid = (low + high) // 2
        merge_sort(data_set, low, mid)
        merge_sort(data_set, mid + 1, high)
        merge(data_set, low, mid, high)



datas = list(range(100))
# print(data_set)
random.shuffle(datas)
(merge_sort(datas))
print(datas)
