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

    if number == 1:
        return 'i'
    if number == 4:
        return 'iv'
    if number == 5:
        return 'v'
    if number == 9:
        return 'ix'
    if number == 10:
        return 'x'
    if number == 40:
        return 'xl'
    if number == 50:
        return 'l'
    if number == 90:
        return 'xcix'
    if number == 100:
        return 'c'
    if number == 400:
        return 'cd'
    if number == 500:
        return 'd'
    if number == 900:
        return 'cmxcix'
    if number == 1000:
        return 'm'

    roman = ''
    while number > 0:
        if number >= 1000:
            roman += 'm'
            number -= 1000
        elif number >= 900:
            roman += 'cm'
            number -= 900
        elif number >= 500:
            roman += 'd'
            number -= 500
        elif number >= 400:
            roman += 'cd'
            number -= 400
        elif number >= 100:
            roman += 'c'
            number -= 100
        elif number >= 90:
            roman += 'xc'
            number -= 90
        elif number >= 50:
            roman += 'l'
            number -= 50
        elif number >= 40:
            roman += 'xl'
            number -= 40
        elif number >= 10:
            roman += 'x'
            number -= 10
        elif number >= 9:
            roman += 'ix'
            number -= 9
        elif number == 5:
            roman += 'v'
        elif number == 4:
            roman += 'iv'
        elif number == 1:
            roman += 'i'
    return roman
