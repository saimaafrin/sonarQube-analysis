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

    romans = 'ivxlcdm'
    roman = []
    num = number
    i = 1
    while num > 0:
        remainder = num % 10
        num //= 10
        roman.append(romans[4 * i + remainder // 5])
        roman.append(romans[4 * i + remainder % 5])
        i += 1
    return ''.join(reversed(roman))
