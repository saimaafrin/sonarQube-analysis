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


    # Solution 1
    count = 0
    for num in arr:
        total = 0
        if num < 0:
            num = -num
            total -= 1
        while num > 0:
            total += num % 10
            num //= 10
        if total > 0:
            count += 1
    return count

    # Solution 2
    return sum(1 for num in arr if abs(sum(int(d) for d in str(num))) > 0)

    # Solution 3
    return sum(1 for num in arr if abs(sum(d**2 for d in str(num))) > 0)
