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

    # factorial
    def fac(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    # check if n is even
    def is_even(n):
        return n % 2 == 0

    # sum 1 + 2 + ... + n
    def sum_n(n):
        return n * (n + 1) // 2

    result = []
    for i in range(1, n+1):
        if is_even(i):
            result.append(fac(i))
        else:
            result.append(sum_n(i))

    return result
