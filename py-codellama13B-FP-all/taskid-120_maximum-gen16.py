from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

    >>> maximum([-3, -4, 5], 3)
    [-4, -3, 5]

    Example 2:

    >>> maximum([4, -4, 4], 2)
    [4, 4]

    Example 3:

    >>> maximum([-3, 2, 1, 2, -1, -2, 1], 1)
    [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """

    if len(arr) == k:
        return sorted(arr)

    # Use a max heap (or priority queue) to quickly retrieve the largest k elements
    max_heap = []
    for i in range(len(arr)):
        if len(max_heap) == k:
            # If the heap has k elements, compare the new element with the top of the heap.
            # If the new element is larger than the top of the heap, add the new element to the heap.
            if arr[i] > max_heap[0]:
                max_heap[0] = arr[i]
                max_heap.heapify()
        else:
            # If the heap has less than k elements, add the new element to the heap.
            max_heap.append(arr[i])
            max_heap.heapify()
    
    # Return a sorted list of the elements in the heap
    return sorted(max_heap)
