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


    # Convert each element to string, split into two substrings
    #   and convert back to int.
    #   If element has one digit, add it.
    #   If element has two digits, add it if it belongs to first k elements.
    return sum(
        [int(sub_element)
        for element in arr
        for sub_element in str(element)
        if (
            len(str(element)) == 1
            or (len(str(element)) == 2 and arr.index(element) < k)
        )]
    )
