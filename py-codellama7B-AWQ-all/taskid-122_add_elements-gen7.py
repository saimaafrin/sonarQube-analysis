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

    # create a hash table to store counts of digits
    counts = {}

    # loop over elements in the first k elements of arr
    for digit in arr[:k]:
        # get the digit as a string
        str_digit = str(digit)

        # if str_digit has length 1 then add it to counts as key with value 1
        if len(str_digit) == 1:
            counts[str_digit] = 1
        # if str_digit has length 2 then add it to counts as key with value 2
        else:
            counts[str_digit[:1]] = counts.get(str_digit[:1], 0) + 1

    # loop over elements in arr
    for digit in arr:
        # get the digit as a string
        str_digit = str(digit)

        # if str_digit has length 1 then add it to counts as key with value 1
        if len(str_digit) == 1:
            counts[str_digit] = 1
        # if str_digit has length 2 then add it to counts as key with value 2
        else:
            counts[str_digit[:1]] = counts.get(str_digit[:1], 0) + 1

    # loop over counts
    for digit, count in counts.items():
        # if count <= 2 then add digit to sum
        if count <= 2:
            sum += int(digit)

    return sum
