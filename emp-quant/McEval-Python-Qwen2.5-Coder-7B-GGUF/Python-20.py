from typing import List 
def polynomial_to_string(n: int, coeffs: List[int]) -> str:
    """
    Converts a list of polynomial coefficients into a formatted string representation.

    The function takes in the highest degree `n` of the polynomial and a list of coefficients `coeffs`,
    which are ordered from the highest degree term to the constant term. It returns a string that
    represents the polynomial with the following rules:
    - Terms with a coefficient of zero are omitted.
    - The sign of each term is determined (+ for positive, - for negative), with no leading '+' for the first term.
    - The absolute value of the coefficient is shown unless it's 1 and the term includes the variable `x`.
    - The variable part is formatted based on its degree; `x^degree` for degree > 1, `x` for degree 1, and
      nothing for degree 0 (constant term).
    - Terms are joined without additional spaces, starting with the highest degree term.

    Args:
        n (int): The highest degree of the polynomial.
        coeffs (List[int]): A list of coefficients, starting with the coefficient of the highest degree term.

    Returns:
        str: The string representation of the polynomial.

    Examples:
        >>> polynomial_to_string(5, [100, -1, 1, -3, 0, 10])
        '100x^5-x^4+x^3-3x^2+10'

        >>> polynomial_to_string(3, [-50, 0, 0, 1])
        '-50x^3+1'
    """


    # Initialize an empty list to store the terms of the polynomial
    terms = []

    # Iterate over the coefficients and their corresponding degrees
    for i in range(n, -1, -1):
        coeff = coeffs[n - i]

        # Skip terms with a coefficient of zero
        if coeff == 0:
            continue

        # Determine the sign of the term
        sign = '+' if coeff > 0 else '-'
        if terms and sign == '+':
            sign = ''

        # Calculate the absolute value of the coefficient
        abs_coeff = abs(coeff)

        # Format the term based on its degree
        if i == 0:
            term = f'{sign}{abs_coeff}' if abs_coeff != 1 else sign
        elif i == 1:
            term = f'{sign}{abs_coeff}x' if abs_coeff != 1 else f'{sign}x'
        else:
            term = f'{sign}{abs_coeff}x^{i}' if abs_coeff != 1 else f'{sign}x^{i}'

        # Add the term to the list of terms
        terms.append(term)

    # Join the terms into a single string and return it
    return ''.join(terms)
def test_polynomial_to_string():
    test_cases = [
        (4, [3, -2, 0, 1, -5], "3x^4-2x^3+x-5"),
        (2, [0, 4, -1], "+4x-1"),
        (0, [7], "7"),
        (3, [1, -1, 0, 1], "x^3-x^2+1"),
    ]

    for i, (n, coeffs, expected) in enumerate(test_cases):
        result = polynomial_to_string(n, coeffs)

        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: expected {expected}, got {result}")


test_polynomial_to_string()