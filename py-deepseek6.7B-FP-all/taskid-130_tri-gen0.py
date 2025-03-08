from typing import List

def tri(n: int) -> List[int]:
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    >>> tri(3)
    [1, 3, 2, 8]
    """

    tri_sequence = [1, 3]
    if n < 1:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return tri_sequence

    for i in range(2, n):
        if tri_sequence[i - 1] % 2 == 0:
            tri_sequence.append(1 + tri_sequence[i - 1] // 2)
        else:
            tri_sequence.append(tri_sequence[i - 1] + tri_sequence[i - 2] + tri_sequence[i] + 1)
    return tri_sequence
