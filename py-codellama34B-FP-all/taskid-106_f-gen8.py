from typing import List

def f(n: int) -> List[int]:
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    >>> f(5)
    [1, 2, 6, 24, 15]
    """

    if n <= 0:
        return []
    return [factorial_of_i_if_i_is_even_or_sum_of_numbers_from_1_to_i_otherwise(i) for i in range(1, n + 1)]
