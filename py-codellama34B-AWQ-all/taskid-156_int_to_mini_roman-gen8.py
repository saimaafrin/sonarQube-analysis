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

    if not 0 < number <= 1000:
        raise ValueError("Number must be between 1 and 1000 inclusive")
    numerals = [
        (1000, "m"),
        (500, "d"),
        (100, "c"),
        (50, "l"),
        (10, "x"),
        (5, "v"),
        (1, "i"),
    ]
    roman = ""
    while number > 0:
        for value, symbol in numerals:
            if number >= value:
                number -= value
                roman += symbol
                break
    return roman
