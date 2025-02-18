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

    roman = ''
    while number >= 1000:
        roman += 'm'
        number -= 1000
    while number >= 900:
        roman += 'cm'
        number -= 900
    while number >= 500:
        roman += 'd'
        number -= 500
    while number >= 400:
        roman += 'cd'
        number -= 400
    while number >= 100:
        roman += 'c'
        number -= 100
    while number >= 90:
        roman += 'xc'
        number -= 90
    while number >= 50:
        roman += 'l'
        number -= 50
    while number >= 40:
        roman += 'xl'
        number -= 40
    while number >= 10:
        roman += 'x'
        number -= 10
    while number >= 9:
        roman += 'ix'
        number -= 9
    while number >= 5:
        roman += 'v'
        number -= 5
    while number >= 4:
        roman += 'iv'
        number -= 4
    while number >= 1:
        roman += 'i'
        number -= 1
    return roman.lower()
