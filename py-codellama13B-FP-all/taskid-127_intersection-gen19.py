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

    # Find the intersection of the two intervals.
    # If one interval completely covers the other,
    # then the intersection is the covered interval.
    # Otherwise, the intersection is the overlap of the two intervals.
    # Return "NO" if the intersection is empty.
    # Otherwise, return "YES" if the length of the intersection is prime, and "NO" otherwise.
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 <= start2:
        if end1 < start2:
            return "NO"
        start, end = start2, min(end1, end2)
    else:
        if end2 < start1:
            return "NO"
        start, end = start1, min(end1, end2)
    length = end - start + 1
    # Check whether the length of the intersection is prime.
    if length == 1:
        return "NO"
    elif length == 2:
        return "YES"
    elif length % 2 == 0:
        return "NO"
    elif length % 3 == 0:
        return "NO"
    elif length % 5 == 0:
        return "NO"
    elif length % 7 == 0:
        return "NO"
    elif length % 11 == 0:
        return "NO"
    elif length % 13 == 0:
        return "NO"
    elif length % 17 == 0:
        return "NO"
    elif length % 19 == 0:
        return "NO"
    else:
        return "YES"
