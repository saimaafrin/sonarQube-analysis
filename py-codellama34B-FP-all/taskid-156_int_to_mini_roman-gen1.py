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

    mini_roman_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman_numeral = ''
    number_str = str(number)
    for index, digit in enumerate(number_str):
        multiplier = 10 ** (len(number_str) - index - 1)
        roman_numeral += int_to_mini_roman_helper(int(digit), multiplier, mini_roman_map)

    return roman_numeral
