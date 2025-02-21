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

    def roman_digit(num: int) -> str:
        return 'i'*num
    roman = ''
    roman += roman_digit(number // 1000)
    roman += roman_digit((number % 1000) // 100)
    roman += roman_digit((number % 100) // 10)
    roman += roman_digit(number % 10)
    return roman
