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

    def factorial(i: int) -> int:
        """ Implement the function factorial that takes i as a parameter,
        and returns the product of the numbers from 1 to i.
        Example:
        >>> factorial(3)
        6
        >>> factorial(4)
        24
        """
        if i <= 1:
            return 1
        else:
            return i * factorial(i - 1)

    def sum_of_numbers(i: int) -> int:
        """ Implement the function sum_of_numbers that takes i as a parameter,
        and returns the sum of the numbers from 1 to i.
        Example:
        >>> sum_of_numbers(3)
        6
        >>> sum_of_numbers(4)
        10
        """
        return sum(range(1, i + 1))

    return [
        factorial(i) if i % 2 == 0 else sum_of_numbers(i) for i in range(1, n + 1)
    ]
