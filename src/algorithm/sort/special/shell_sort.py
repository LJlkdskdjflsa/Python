def insert_sort_gap(data_set: list[int],gap:int) -> list[int]:
    """insert_sort_gap
    insert sort with gap

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
    for i in range(gap, len(data_set)):  # the index of new select
        tmp = data_set[i]
        j = i - gap  # the index of sorted
        while j >= 0 and data_set[j] > tmp:  # linear search
            data_set[j + gap] = data_set[j]
            j -= gap
        data_set[j + gap] = tmp
    return data_set

def shell_sort(data_set: list[int])->list[int]:
    """shell sort
    every time do a select sort in gap,
    the gap loop through the lengh of list

    Time Complexity is related to the gap you choose

    Args:
        data_set (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    d = len(data_set) // 2
    while d >= 1:
        insert_sort_gap(data_set,d)
        d //= 2

    return data_set


