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

    total = 0
    for num in arr:
        signed_digits = []
        if num < 0:
            signed_digits.append(-1)
        while abs(num) > 0:
            signed_digits.append(abs(num) % 10)
            num = abs(num) // 10
        if sum(signed_digits) > 0:
            total += 1
    return total
