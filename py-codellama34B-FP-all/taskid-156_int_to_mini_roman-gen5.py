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

    # sanity check
    if not 1 <= number <= 1000:
        raise ValueError('Number must be between 1 and 1000 inclusive')

    # convert each digit in the number to roman numeral, and append it
    # to a string.
    roman_numeral = ''
    for i, digit in enumerate(str(number)):
        roman_numeral += _DIGIT_TO_ROMAN_NUMERAL_MAP[digit][i]

    # return the roman numeral string
    return roman_numeral
