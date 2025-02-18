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

    roman_numerals = {
        # key: (value, times repeated)
        1000: ("m", 1),
        900: ("cm", 1),
        500: ("d", 1),
        400: ("cd", 1),
        100: ("c", 1),
        90: ("xc", 1),
        50: ("l", 1),
        40: ("xl", 1),
        10: ("x", 1),
        9: ("ix", 1),
        5: ("v", 1),
        4: ("iv", 1),
        1: ("i", 1),
    }
    result = ""
    for value, (numeral, multiplier) in roman_numerals.items():
        while number >= value:
            number -= value
            result += numeral * multiplier
    return result
