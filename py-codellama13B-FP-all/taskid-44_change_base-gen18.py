def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    # Check that base is valid
    assert 2 <= base <= 9, "Base must be between 2 and 9"

    # Special case for x=0
    if x == 0:
        return "0"

    # Initialize result
    result = ""

    # Iterate until x becomes 0
    while x > 0:
        result = f"{x % base}" + result
        x //= base

    # Return result
    return result
