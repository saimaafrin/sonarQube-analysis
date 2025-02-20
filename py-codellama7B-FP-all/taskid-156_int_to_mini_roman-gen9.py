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

    roman_num = ''
    while number > 0:
        if number % 10 == 9:
            roman_num += 'ix'
            number -= 9
        elif number % 10 == 8:
            roman_num += 'viii'
            number -= 8
        elif number % 10 == 7:
            roman_num += 'vii'
            number -= 7
        elif number % 10 == 6:
            roman_num += 'vi'
            number -= 6
        elif number % 10 == 5:
            roman_num += 'v'
            number -= 5
        elif number % 10 == 4:
            roman_num += 'iv'
            number -= 4
        elif number % 10 == 3:
            roman_num += 'iii'
            number -= 3
        elif number % 10 == 2:
            roman_num += 'ii'
            number -= 2
        elif number % 10 == 1:
            roman_num += 'i'
            number -= 1

    return roman_num
