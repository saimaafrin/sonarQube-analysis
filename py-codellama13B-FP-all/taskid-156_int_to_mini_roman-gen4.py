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
        'm': 1000,
        'd': 500,
        'c': 100,
        'l': 50,
        'x': 10,
        'v': 5,
        'i': 1,
    }

    if number == 0:
        return ''
    elif number > 1000:
        raise ValueError('Invalid input: Only valid for 1 <= num <= 1000')

    roman_numeral = ''

    for numeral, value in roman_numerals.items():
        while number >= value:
            number -= value
            roman_numeral += numeral

    return roman_numeral
