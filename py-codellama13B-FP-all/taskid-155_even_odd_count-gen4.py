from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """


    str_num = str(abs(num))
    count_even = 0
    count_odd = 0

    for digit in str_num:
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return (count_even, count_odd)
