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


    # This function takes two tuples as arguments and returns the
    # length of the intersection of the two intervals, if the two
    # intervals do not intersect, it returns 0.
    def intersection_length(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> int:
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start <= end:
            return end - start
        else:
            return 0

    # This function takes a number as argument and returns "YES"
    # if the number is a prime number, otherwise, it returns "NO"
    def is_prime(n: int) -> str:
        if n < 2:
            return 'NO'
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 'NO'
        return 'YES'

    intersection_len = intersection_length(interval1, interval2)
    if intersection_len == 0:
        return 'NO'
    else:
        return is_prime(intersection_len)
