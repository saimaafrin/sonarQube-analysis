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

    def factorial(n: int) -> int:
        """ The function that calculates factorial of n. """
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def sum_of_numbers(n: int) -> int:
        """ The function that calculates the sum of numbers from 1 to n. """
        result = 0
        for i in range(1, n + 1):
            result += i
        return result

    result: List[int] = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_of_numbers(i))
    return result
