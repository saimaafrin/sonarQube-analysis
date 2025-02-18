def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """

    # Convert integer to a string
    str_num = str(n)

    # Loop through each character in the string, which is a digit
    product = 1
    for digit in str_num:

        # Check if the current digit is odd
        if int(digit) % 2 != 0:

            # Multiply the product by the current digit
            product *= int(digit)

    return product
