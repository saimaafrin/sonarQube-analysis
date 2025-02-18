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

    if number < 1 or number > 1000:
        raise ValueError("number must be in range [1, 1000]")

    # Dict mapping digits to their corresponding roman numeral equivalents
    roman_numerals = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
    }

    result = ""

    while number > 0:
        for digit in range(1, 10):
            if number >= digit * 10:
                number -= digit * 10
                result += roman_numerals[digit * 10]
                break

    return result
