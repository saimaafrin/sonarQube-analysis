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


    def _get_roman_numeral(num: int, base_numeral: str) -> str:
        return base_numeral * num

    if number < 1 or number > 1000:
        raise ValueError("Number must be positive and less than 1000")

    roman_numerals = []

    if number // 100 > 0:
        roman_numerals.append("c" * (number // 100))
        number %= 100

    if number // 10 == 9:
        roman_numerals.append("xc")
        number %= 10
    elif number // 10 > 5:
        roman_numerals.append("l" * (number // 10 - 5))
        number %= 10
    elif number // 10 > 0:
        roman_numerals.append("x" * (number // 10))
        number %= 10

    if number == 9:
        roman_numerals.append("ix")
    elif number > 5:
        roman_numerals.append("v" * (number - 5))
    elif number > 0:
        roman_numerals.append("i" * number)

    return "".join(roman_numerals)
