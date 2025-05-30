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

    # finding the intersection
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])

    # finding the length of intersection
    intersection_length = intersection_end - intersection_start + 1 if intersection_end >= intersection_start else 0

    # checking if the intersection's length is a prime number
    if intersection_length == 0:
        return "NO"
    elif intersection_length == 1:
        return "NO"
    elif intersection_length == 2:
        return "NO"
    else:
        for i in range(2, int(intersection_length**0.5)+1):
            if intersection_length % i == 0:
                return "NO"
        return "YES"
