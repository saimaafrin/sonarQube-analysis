from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """


    digits = [int(x) for x in str(abs(num))]
    even_cnt = 0
    odd_cnt = 0

    for digit in digits:
        if digit % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1

    return (even_cnt, odd_cnt)
