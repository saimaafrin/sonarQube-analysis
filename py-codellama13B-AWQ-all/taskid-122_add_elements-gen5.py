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


    arr = arr[:k]
    arr_sum = sum(arr)
    arr_sum_with_two_digits = 0
    for element in arr:
        element_sum = sum(str(element))
        if element_sum <= 2:
            arr_sum_with_two_digits += element_sum
        else:
            arr_sum_with_two_digits += 2
    return arr_sum_with_two_digits + arr_sum
