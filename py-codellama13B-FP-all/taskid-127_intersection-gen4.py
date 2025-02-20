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

    # [1, 2] and [2, 3]
    # [1, 3] and [2, 4]
    # [1, 3] and [1, 3]
    # [1, 4] and [2, 3]
    # [1, 4] and [1, 4]
    # [1, 3] and [1, 4]
    # [1, 3] and [2, 4]
    # [2, 4] and [1, 4]
    start, end = interval1
    start2, end2 = interval2
    if end < start2 or end2 < start:
        return "NO"
    if start <= start2 <= end or start2 <= start <= end2:
        return "YES" if is_prime(end - start2 + 1) else "NO"
    return "YES" if is_prime(end - start + 1) else "NO"
