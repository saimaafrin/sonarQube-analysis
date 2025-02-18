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

    result = ''
    while number > 0:
        if number >= 1000:
            number -= 1000
            result += 'm'
        elif number >= 900:
            number -= 900
            result += 'cm'
        elif number >= 500:
            number -= 500
            result += 'd'
        elif number >= 400:
            number -= 400
            result += 'cd'
        elif number >= 100:
            number -= 100
            result += 'c'
        elif number >= 90:
            number -= 90
            result += 'xc'
        elif number >= 50:
            number -= 50
            result += 'l'
        elif number >= 40:
            number -= 40
            result += 'xl'
        elif number >= 10:
            number -= 10
            result += 'x'
        elif number >= 9:
            number -= 9
            result += 'ix'
        elif number >= 5:
            number -= 5
            result += 'v'
        elif number >= 4:
            number -= 4
            result += 'iv'
        else:
            number -= 1
            result += 'i'
    return result
