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


    # Time: O(n + klog(k))
    # Space: O(k)
    def max_heapify(arr: List[int], k: int, index: int) -> None:
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index

        if left < k and arr[left] > arr[largest]:
            largest = left
        if right < k and arr[right] > arr[largest]:
            largest = right

        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            max_heapify(arr, k, largest)

    def build_max_heap(arr: List[int], k: int) -> None:
        for index in range(k // 2, -1, -1):
            max_heapify(arr, k, index)

    kth = k - 1
    build_max_heap(arr, kth)
    for i in range(k, len(arr)):
        if arr[i] > arr[0]:
            arr[i], arr[0] = arr[0], arr[i]
            max_heapify(arr, kth, 0)

    return arr[:k]
