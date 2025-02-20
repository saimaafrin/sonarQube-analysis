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

    if number < 1 or number > 1000:
        raise ValueError('number must be between 1 and 1000 inclusive')
    roman_numerals = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    roman_digits = [roman_numerals[i] for i in sorted(roman_numerals, reverse=True)]
    roman_str = ''
    while number > 0:
        for digit, roman in zip(roman_digits, roman_digits[1:] + [None]):
            if number >= digit:
                if number == digit:
                    roman_str += roman
                    break
                elif number < 4 * digit:
                    roman_str += digit * (number // digit)
                    number %= digit
                else:
                    roman_str += roman + (digit * (number // digit - 1))
                    number %= digit
                break
    return roman_str
