# Top K Question

There are N numbers , calculate the higher k numbers (k< n)

Resolve Ways:
- Sort than Slice -> O(n*log(n))
- bubble,select,insert sort -> O(k*n)
- heap sort -> O(n*log(k))

## Use Heap Sort to solve the problem

- get the first k elements of the list to make a Min Heap(the root is the number k high element)(小根堆)
- backward loop through the list, if element is higher than root, than change root to the element, and make an adjestment to the heap
- after loop through the list, backward pop elements out