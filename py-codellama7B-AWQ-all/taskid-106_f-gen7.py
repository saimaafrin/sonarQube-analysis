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

    # YOUR CODE HERE
    lst = [1] * n
    for i in range(1, n):
        if i % 2 == 0:
            lst[i] = lst[i-1] * i
        else:
            lst[i] = sum(range(1, i+1))
    return lst
\end{code}
