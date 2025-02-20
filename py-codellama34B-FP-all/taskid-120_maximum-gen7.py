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


    n = len(arr)
    k = min(n, k)

    def partition(low, high, k):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] >= pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]

        return i

    def find_kth_largest(low, high, k):
        if k > 0 and k <= high - low + 1:
            pos = partition(low, high, k)
            if pos - low == k - 1:
                return pos
            elif pos - low > k - 1:
                return find_kth_largest(low, pos - 1, k)
            else:
                return find_kth_largest(pos + 1, high, k - pos + low - 1)
        else:
            return -1

    find_kth_largest(0, n - 1, k)

    return arr[:k]
