# pyright: strict


from random import random
from algorithm.search.binary_search.binary_search import binary_search
from algorithm.search.linear_search.linear_search import linear_search

value_range = 1000000
data_set = list(range(1,value_range ))
target_value = int(random() * value_range)
binary_search(data_set, target_value)
linear_search(data_set, target_value)
