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


    start_i1, end_i1 = interval1
    start_i2, end_i2 = interval2
    i1 = start_i1
    i2 = start_i2
    if (end_i1 < start_i2) or (start_i1 > end_i2):
        return "NO"
    else:
        if (start_i1 <= start_i2 and end_i1 >= start_i2) or (start_i1 <= end_i2 and end_i1 >= end_i2):
            i1 = max(start_i1, start_i2)
            i2 = min(end_i1, end_i2)

    return ("YES" if len(range(i1, i2 + 1)) > 1 else "NO")
