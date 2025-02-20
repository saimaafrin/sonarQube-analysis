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

    if not (1 <= number <= 1000):
        raise ValueError('Number not in range 1-1000')

    if number == 1000:
        return 'm' * 4

    roman_num = ''

    while number > 0:
        if number >= 100:
            roman_num += 'c' * (number // 100)
            number %= 100
        elif number >= 90:
            roman_num += 'xc'
            number %= 10
        elif number >= 50:
            roman_num += 'l'
            number %= 50
        elif number >= 40:
            roman_num += 'xl'
            number %= 10
        elif number >= 10:
            roman_num += 'x' * (number // 10)
            number %= 10
        elif number >= 9:
            roman_num += 'ix'
        elif number >= 5:
            roman_num += 'v'
            number %= 5
        elif number >= 4:
            roman_num += 'iv'
        else:
            roman_num += 'i' * number
            number = 0

    return roman_num
