from typing import List

def derivative(xs: List[int]) -> List[int]:
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # write your code here
    n = len(xs)
    if n == 0:
        return []

    # calculate derivative with the previous result
    derivative_array = [0] * n
    for i in range(n):
        derivative_array[i] = i * xs[i]
        if i > 1:
            derivative_array[i] += derivative_array[i - 1]

    return derivative_array
