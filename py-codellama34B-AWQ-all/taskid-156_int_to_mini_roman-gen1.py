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

    roman = ""
    if number >= 500:
        number -= 500
        roman += "d"

    if number >= 100:
        number -= 100
        roman += "c"

    if number >= 50:
        number -= 50
        roman += "l"

    if number >= 10:
        number -= 10
        roman += "x"

    if number >= 5:
        number -= 5
        roman += "v"

    if number >= 1:
        number -= 1
        roman += "i"

    return roman
