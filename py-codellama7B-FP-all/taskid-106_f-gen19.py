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


    def fact(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fact(n-1)

    def sum_numbers(n):
        return sum(range(1, n+1))

    return [fact(i) if i % 2 == 0 else sum_numbers(i) for i in range(1, n+1)]
