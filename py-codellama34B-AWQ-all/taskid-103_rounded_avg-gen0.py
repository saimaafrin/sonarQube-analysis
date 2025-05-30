from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    >>> rounded_avg(1, 5)
    '0b11'
    >>> rounded_avg(7, 5)
    -1
    >>> rounded_avg(10, 20)
    '0b1111'
    >>> rounded_avg(20, 33)
    '0b11010'
    """

    if n > m:
        return -1
    avg = (m + n) // 2
    return f'0b{bin(avg)[2:]}'
