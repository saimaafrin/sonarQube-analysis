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

    # Please add your code here
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * factorial(i))
        else:
            result.append(sum([j for j in range(1, i + 1)]))
    return result
