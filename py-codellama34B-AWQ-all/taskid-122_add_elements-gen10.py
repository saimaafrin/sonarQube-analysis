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


    # two digit numbers, can only have 90 numbers
    max_number = 90

    # count of numbers < 10
    count_less_than_10 = 0

    # count of numbers >= 10 and <= 90
    count_greater_than_10 = 0

    # count of numbers >= 100
    count_greater_than_100 = 0

    # go through first k elements
    for num in arr[:k]:
        # if number is < 10
        if num < 10:
            count_less_than_10 += 1
        # if number is >= 10 and <= 90
        elif num <= max_number:
            count_greater_than_10 += 1
        # if number is >= 100
        else:
            count_greater_than_100 += 1

    # return the sum of all elements, since we can only have 90 numbers,
    # we can ignore the count of numbers >= 100
    return sum(arr[:k]) - (count_greater_than_100 * 90)
