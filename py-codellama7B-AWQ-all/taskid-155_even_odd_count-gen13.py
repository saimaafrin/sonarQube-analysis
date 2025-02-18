from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    count = 0
    for i in str(abs(num)):
        if i % 2 == 0:
            count += 1
    return count, len(str(abs(num))) - count
\end{code}
