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
    # TODO: Implement this function
    # Hint: You can use the `join` method to join a list of strings.
    # Hint: You can use the `format` method to format a string with a variable.
    # Hint: You can use the `abs` function to get the absolute value of a number.
    # Hint: You can use the `bool` function to convert a number to a boolean.
    # Hint: You can use the `+` operator to concatenate strings.
    # Hint: You can use the `*` operator to repeat a string.
    # Hint: You can use the `enumerate` function to iterate over a list and its indices.
    # Hint: You can use the `range` function to create a range of numbers.
    # Hint: You can use the `reversed` function to iterate over a list in reverse.
    # Hint: You can use the `zip` function to combine two lists.
    # Hint: You can use the `map` function to apply a function to each element of a list.
    # Hint: You can use the `filter` function to filter a list based on a condition.
    # Hint: You can use the `sum` function to sum up the elements of a list.
    # Hint: You can use the `sorted` function to sort a list.
    # Hint: You can use the `any` function to check if any element of a list satisfies a condition.
    # Hint: You can use the `all` function to check if all elements of a list satisfy a condition.
    # Hint: You can use the `max` function to find the maximum element of a list.
    # Hint: You can use the `min` function to find the minimum element of a list.
    # Hint: You can use the `len` function to get the length of a list.
    # Hint: You can use the `type` function to get the type of an object.
    # Hint: You can use the `isinstance` function to check if an object is an instance of a class.
    # Hint: You can use the `dir` function to get the attributes of an object.
    # Hint: You can use the `help` function to get help on a function or class.
    # Hint: You can use the `repr` function to get the string representation of an object.
    # Hint: You can use the `eval` function to evaluate a string as Python code.
    # Hint: You can use the `exec` function to execute a string as Python code.
    # Hint: You can use the `open` function to open a file.
    # Hint: You can use the `read` method
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