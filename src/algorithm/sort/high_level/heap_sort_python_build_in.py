import heapq
import random

data_set = list(range(100))
# print(data_set)
random.shuffle(data_set)
# print(data_set)

heapq.heapify(data_set)  # build heap
# print(data_set)

for i in range(len(data_set)):
    print(heapq.heappop(data_set))
