# pyright: strict


# 01 search
# from random import random
# from algorithm.search.binary_search.binary_search import binary_search
# from algorithm.search.linear_search.linear_search import linear_search
# value_range = 1000000
# data_set = list(range(1,value_range ))
# target_value = int(random() * value_range)
# binary_search(data_set, target_value)
# linear_search(data_set, target_value)

# 02 sort
from random import randint
from algorithm.sort.high_level.sort import quick_sort
from algorithm.sort.low_level.sort import (
    bubble_sort,
    insert_sort_binary_search,
    select_sort,
    insert_sort,
)
import copy

data_set_origin = [randint(0, 10000) for i in range(10000)]
answer = copy.deepcopy(data_set_origin)
answer.sort()
print(
    "bubble sort answer is correct:",
    answer == bubble_sort(copy.deepcopy(data_set_origin)),
)
print(
    "select sort answer is correct:",
    answer == select_sort(copy.deepcopy(data_set_origin)),
)
print(
    "select sort answer is correct:",
    answer == insert_sort(copy.deepcopy(data_set_origin)),
)
print(
    "select sort answer is correct:",
    answer == quick_sort(copy.deepcopy(data_set_origin)),
)
# Not Finished yet the binary search still need to be tested
# print(answer)
# print(
#    "select sort answer is correct:",
#    answer == insert_sort_binary_search(copy.deepcopy(data_set_origin)),
# )
