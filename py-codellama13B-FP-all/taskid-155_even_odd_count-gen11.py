from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    odd = 0
    even = 0
    str_num = str(abs(num))
    for i in range(len(str_num)):
        if str_num[i].isdigit():
            if str_num[i] in "02468":
                even += 1
            else:
                odd += 1
    return (even, odd)
