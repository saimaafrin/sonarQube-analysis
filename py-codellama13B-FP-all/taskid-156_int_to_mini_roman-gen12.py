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

    roman_numerals_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    def roman_numeral_helper(number: int, current_roman_numeral: str = '') -> str:
        if number == 0:
            return current_roman_numeral

        for numeral in roman_numerals_map:
            if number - numeral >= 0:
                number -= numeral
                current_roman_numeral += roman_numerals_map[numeral]
                return roman_numeral_helper(number, current_roman_numeral)

    return roman_numeral_helper(number)
