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

    # check if intervals don't overlap
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"

    # get the intersection of the intervals
    intersection = (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))

    # check if the length of the intersection is a prime number
    # (check if the number is positive, is odd, and is divisible only by 1 and itself)
    is_prime = (
        intersection[1] - intersection[0] > 0 and
        intersection[1] - intersection[0] % 2 == 1 and
        (
            intersection[1] - intersection[0] == 1 or
            intersection[1] - intersection[0] % 3 == 0 or
            intersection[1] - intersection[0] % 5 == 0 or
            intersection[1] - intersection[0] % 7 == 0 or
            intersection[1] - intersection[0] % 11 == 0 or
            intersection[1] - intersection[0] % 13 == 0 or
            intersection[1] - intersection[0] % 17 == 0 or
            intersection[1] - intersection[0] % 19 == 0 or
            intersection[1] - intersection[0] % 23 == 0 or
            intersection[1] - intersection[0] % 29 == 0 or
            intersection[1] - intersection[0] % 31 == 0 or
            intersection[1] - intersection[0] % 37 == 0 or
            intersection[1] - intersection[0] % 41 == 0 or
            intersection[1] - intersection[0] % 43 == 0 or
            intersection[1] - intersection[0] % 47 == 0 or
            intersection[1] - intersection[0] % 53 == 0 or
            intersection[1] - intersection[0] % 59 == 0 or
            intersection[1] - intersection[0] % 61 == 0 or
            intersection[1] - intersection[0] % 67 == 0 or
            intersection[1] - intersection[0] % 71 == 0 or
            intersection[1] - intersection[0] % 73 == 0 or
            intersection[1] - intersection[0] % 79 == 0 or
            intersection[1] - intersection[0] % 83 == 0 or
            intersection[1] - intersection[0] % 89 == 0 or
            intersection[1] - intersection[0] % 97 == 0 or
            intersection[1] - intersection[0] % 101 == 0 or
            intersection[1] - intersection[0] % 103 == 0 or
            intersection[1] - intersection[0] % 107 == 0 or
            intersection[1] - intersection[0] % 109 == 0 or
            intersection[1] - intersection[0
