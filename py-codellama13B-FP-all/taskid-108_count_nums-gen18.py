from typing import List

def count_nums(arr: List[int]) -> int:
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([])
    0
    >>> count_nums([-1, 11, -11])
    1
    >>> count_nums([1, 1, 2])
    3
    """

    count = 0
    for num in arr:
        # If the number is negative, its first signed digit will be negative
        if num < 0:
            # num = -123 = -1 - 2 - 3
            # num_sum = -1 + 2 + 3 = 4 > 0
            num_sum = sum(int(digit) for digit in str(num))
        else:
            num_sum = sum(int(digit) for digit in str(num))
        if num_sum > 0:
            count += 1
    return count
