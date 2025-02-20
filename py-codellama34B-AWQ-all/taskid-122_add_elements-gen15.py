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


    result = 0

    # Iterate through the first k elements of arr
    for element in arr[:k]:
        # If the element has two digits or less, add it to the result
        if element // 10 == 0 or element // 100 == 0:
            result += element

    return result
