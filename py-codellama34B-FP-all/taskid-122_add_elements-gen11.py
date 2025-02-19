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


    # create a set of elements with more than 2 digits
    more_than_2_digits = set()
    for element in arr:
        if element >= 100:
            more_than_2_digits.add(element)

    # create a list of elements with less than or equal to 2 digits
    # and add the ones with more than 2 digits
    less_than_2_digits = []
    for element in arr:
        if element not in more_than_2_digits:
            less_than_2_digits.append(element)

    # sort the list of elements with less than or equal to 2 digits
    # and add the k elements
    less_than_2_digits.sort()
    sum_of_elements = sum(less_than_2_digits[0:k])

    return sum_of_elements
