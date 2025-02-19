from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-1, 1), (0, 4))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """

    from math import isqrt
    a1, a2 = interval1
    b1, b2 = interval2
    c1, c2 = max(a1, b1), min(a2, b2)
    if c1 > c2:
        return 'NO'
    # for x > 3, there are 2 prime numbers
    # less than √x, 2 and x-2, this is why x-4
    if c2 - c1 > 4:
        return 'NO'
    c = c2 - c1 + 1
    return 'YES' if c > 2 and all(c % i for i in range(2, isqrt(c) + 1)) else 'NO'
