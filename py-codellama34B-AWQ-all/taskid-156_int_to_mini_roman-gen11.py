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

    if not (0 < number <= 1000):
        raise ValueError(f"{number} is not a valid roman numeral")

    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    mini_roman_numerals = dict((val, key) for key, val in roman_numerals.items())

    mini_roman_numeral = ''
    while number > 0:
        for r in range(1000, 1, -1):
            if number >= r:
                number -= r
                mini_roman_numeral += mini_roman_numerals[r]
                break
    return mini_roman_numeral
