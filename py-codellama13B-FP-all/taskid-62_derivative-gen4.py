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

    # this was the original solution:
    # return [x * y for x, y in zip(xs[1:], xs)]

    # this is a better solution, less memory usage
    # as we only have to store the current derivative
    # instead of the full polynomial
    if len(xs) == 1:
        return [0]
    return [x * y for x, y in zip(xs[1:], xs)]
