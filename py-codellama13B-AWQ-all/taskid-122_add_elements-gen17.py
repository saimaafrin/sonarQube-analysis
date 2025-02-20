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

    arr.sort()
    first_two = [arr[0], arr[1]]
    two_digits = 0
    for i in range(k):
        if len(str(arr[i])) == 2:
            two_digits += arr[i]
        else:
            two_digits += first_two[0]
            first_two.pop(0)
            first_two.append(arr[i])
    return two_digits
