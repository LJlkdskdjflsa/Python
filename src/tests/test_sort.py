# pyright: strict
from copy import deepcopy
from random import randint
from sys import path

import pytest
from algorithm.sort.high_level.sort import partition, quick_sort

path.append("..")


@pytest.fixture(name="get_data_and_answer")
def fixture_get_data_and_answer() -> tuple[list[int], list[int]]:
    """get_data_and_answer

    Returns:
        tuple[list[int], list[int]]: original data, answer
    """
    data_set_origin = [randint(0, 10000) for i in range(10)]
    answer = deepcopy(data_set_origin)
    answer.sort()
    return data_set_origin, answer


# quick_sort
def test_quick_sort(get_data_and_answer: tuple[list[int], list[int]]):
    data_set_origin, answer = get_data_and_answer
    assert quick_sort(data_set_origin) == answer


def test_partition(get_data_and_answer: tuple[list[int], list[int]]):
    """test partition function works correctly
    seperate smaller and bigger items of the list to the left and right side of middle one

    Args:
        get_data_and_answer (tuple[list[int], list[int]]):  original data
    """
    data_set_origin, _ = get_data_and_answer
    middle_index = partition(data_set_origin, 0, len(data_set_origin) - 1)
    middle_value = data_set_origin[middle_index]

    # check the value of left and right is smaller and greater than middle_value
    for index, value in enumerate(data_set_origin):
        if index < middle_index:
            assert value <= middle_value
        elif index > middle_index:
            assert value >= middle_value
