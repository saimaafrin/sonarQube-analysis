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


    # Intervals are (start, end)
    i1_start, i1_end = interval1
    i2_start, i2_end = interval2
    # Case when intervals don't intersect
    if i1_start > i2_end or i2_start > i1_end:
        return "NO"

    # Calculate the length of the intersection
    intersection_length = min(i1_end, i2_end) - max(i1_start, i2_start) + 1

    # Check if length of intersection is a prime number
    if intersection_length > 1 and intersection_length % 2 != 0 and intersection_length % 3 != 0 and intersection_length % 5 != 0 and intersection_length % 7 != 0:
        return "YES"
    else:
        return "NO"
