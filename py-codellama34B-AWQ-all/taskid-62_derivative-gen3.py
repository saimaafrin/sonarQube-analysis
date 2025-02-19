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

    # The derivative of the polynomial p is given by:
    #
    # p' = sum(i * p_i * x^(i-1))
    #
    # so for a polynomial of degree n, the derivative will be a polynomial
    # of degree n-1.  To compute the derivative, we'll need to iterate
    # over every pair of adjacent coefficients and multiply them together.
    # Then we'll shift the coefficients down by one, dropping the last
    # one.

    # TODO: Compute and return the derivative
    # Hint: you may find enumerate() useful
    if len(xs) == 0:
        return []
    result = [0] * (len(xs) - 1)
    for index, val in enumerate(xs):
        if index != 0:
            result[index - 1] = val * index
    return result
