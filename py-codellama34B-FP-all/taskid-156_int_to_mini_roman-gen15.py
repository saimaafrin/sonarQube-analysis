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

    MINI_ROMAN_MAP = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    roman_number = ""
    while number > 0:
        for roman_val in sorted(MINI_ROMAN_MAP.values(), reverse=True):
            if number >= int(roman_val):
                number -= int(roman_val)
                roman_number += roman_val
                break
    return roman_number.lower()
