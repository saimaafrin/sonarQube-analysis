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

    roman_numeral_string = ''
    thousands_place = number // 1000
    hundreds_place = number % 1000 // 100
    tens_place = number % 100 // 10
    ones_place = number % 10

    roman_numeral_string += 'm' * thousands_place
    roman_numeral_string += roman_numeral_map[hundreds_place]
    roman_numeral_string += roman_numeral_map[tens_place]
    roman_numeral_string += roman_numeral_map[ones_place]
    return roman_numeral_string
