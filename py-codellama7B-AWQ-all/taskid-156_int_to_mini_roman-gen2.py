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

    MINI_ROMAN_DIGITS = {1: "i", 4: "iv", 5: "v", 9: "ix"}
    roman = ""
    for place, value in enumerate(reversed(str(number))):
        value = int(value)
        if place == 0:
            roman += value * "i"
        else:
            if value == 9:
                roman += "ix"
            elif value == 5:
                roman += "v"
            elif value == 4:
                roman += "iv"
            else:
                roman += str(value) * "i"
    return roman
