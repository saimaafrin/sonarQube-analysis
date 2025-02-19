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


    # Heap sort
    # Time: O(nlogk)
    # Space: O(k)
    def heap_sort(arr, k):
        import heapq
        heapq.heapify(arr)
        return heapq.nlargest(k, arr)
    
    # Quick select
    # Time: O(n) ~ O(n^2)
    # Space: O(1)
    def quick_select(arr, k):
        left, right = 0, len(arr) - 1
        while True:
            pivot = partition(arr, left, right)
            if pivot == k - 1:
                return arr[:k]
            elif pivot < k - 1:
                left = pivot + 1
            else:
                right = pivot - 1

    # Partition
    def partition(arr, left, right):
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left
    
    return heap_sort(arr, k)
