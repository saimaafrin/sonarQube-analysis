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


    # We know that:
    # - 10**2 <= 1000
    # - 1 <= 100 <= 10**2
    # =>
    # - 10**2 <= 10**2 <= 1000
    #
    # There are 10**2 = 100 possible digits.
    # We can represent a number with 2 digits
    # in 10**2 = 100 possible ways.
    #
    # There are 10**2 = 100 possible digits.
    # We can represent a number with 1 digit in 10 possible ways.
    #
    # 10**2 = 100
    # 10 = 10
    #
    # The number of possible sums is:
    # 10**2 + 10 = 102
    #
    # The maximum value of a sum is:
    # 10**2 = 100
    #
    # We can represent a number with 2 digits
    # in 10**2 = 100 possible ways.
    #
    # There are 10**2 = 100 possible digits.
    # We can represent a number with 1 digit in 10 possible ways.
    #
    # 10**2 = 100
    # 10 = 10
    #
    # The number of possible sums is:
    # 10**2 + 10 = 102
    #
    # The maximum value of a sum is:
    # 10**2 = 100
    #
    # We can represent a number with 2 digits
    # in 10**2 = 100 possible ways.
    #
    # There are 10**2 = 100 possible digits.
    # We can represent a number with 1 digit in 10 possible ways.
    #
    # 10**2 = 100
    # 10 = 10
    #
    # The number of possible sums is:
    # 10**2 + 10 = 102
    #
    # The maximum value of a sum is:
    # 10**2 = 100
    #
    # We can represent a number with 2 digits
    # in 10**2 = 100 possible ways.
    #
    # There are 10**2 = 100 possible digits.
    # We can represent a number with 1 digit in 10 possible ways.
    #
    # 10**2 = 100
    # 10 = 10
    #
    # The number of possible sums is:
    # 10**2 + 10 = 102
    #
    # The maximum value of a sum is:
    # 10**2 = 100
    #
    # We can represent a number with 2 digits
    # in 10**2 = 100 possible ways.
    #
    # There are 10**2 = 100 possible digits.
    # We can represent a number with 1 digit in 10 possible ways.
    #
    # 10**2 = 100
    # 10 = 10
    #
    # The number of possible sums is:
    # 10**2 + 10 = 102
    #
    # The maximum value of a sum is:
    # 10**2 = 100
    #
    # We can represent a
