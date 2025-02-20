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


    # init max_heap
    heap = []

    # init index
    idx = 0

    # init result
    result = []

    # loop while k > 0
    while k > 0:

        # check if arr[idx] exist
        if idx >= len(arr):
            break

        # check if arr[idx] is greater than the first item of heap
        if arr[idx] > heap[0] if heap else 0:

            # add arr[idx] to heap
            heapq.heappush(heap, arr[idx])

        # increment idx
        idx += 1

    # loop while k > 0
    while k > 0:

        # check if heap is empty
        if not heap:
            break

        # add first item of heap to result
        result.append(heapq.heappop(heap))

        # decrement k
        k -= 1

    # return result
    return result
