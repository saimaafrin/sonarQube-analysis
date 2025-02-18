def int_to_mini_roman(number: int) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """

    # Use a dictionary to map each number to its corresponding Roman numeral
    # symbol.
    ROMAN_NUMERALS = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i"
    }

    result = ""
    for value, numeral in ROMAN_NUMERALS.items():
        # Use the modulo operator to obtain the integer quotient and remainder.
        quotient, remainder = divmod(number, value)
        result += numeral * quotient
        number = remainder

    # Return the Roman numeral equivalent of the input integer.
    return result
