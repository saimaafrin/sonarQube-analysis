from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    # Use a heap to keep track of the k smallest elements
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])

    # Keep track of the sum of the smallest elements
    smallest_sum = sum(heap)
    for i in range(k, len(arr)):
        # If the smallest element is larger than the current element,
        # remove the smallest element and add the current element.
        smallest_element = heapq.heappop(heap)
        if smallest_element > arr[i]:
            smallest_sum -= smallest_element
            smallest_sum += arr[i]
        else:
            # If the smallest element is smaller than the current element,
            # add the current element.
            smallest_sum += arr[i]
        heapq.heappush(heap, arr[i])
    return smallest_sum
