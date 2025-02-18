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

    mini_romans = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xli', 'x', 'ix', 'v', 'iv', 'i']
    quotients, remainder = divmod(number, 1000)
    roman_numeral = ''
    for i in range(quotients):
        roman_numeral += 'm'
    if remainder > 0:
        roman_numeral += mini_romans[remainder - 1]
    return roman_numeral
