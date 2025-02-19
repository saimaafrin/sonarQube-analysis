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

    if not isinstance(number, int):
        raise ValueError('Expected a positive integer.')

    if number < 1 or number > 1000:
        raise ValueError('Expected a positive integer within range of 1 to 1000.')

    if number < 4:
        return 'i' * number

    if number == 4:
        return 'iv'

    if number == 5:
        return 'v'

    if number < 9:
        return 'v' + 'i' * (number - 5)

    if number == 9:
        return 'ix'

    if number < 40:
        return 'x' * (number // 10) + int_to_mini_roman(number % 10)

    if number == 40:
        return 'xl'

    if number < 90:
        return 'xl' + int_to_mini_roman(number - 40)

    if number == 90:
        return 'xci'

    if number < 400:
        return 'x' * (number // 100) + int_to_mini_roman(number % 100)

    if number == 400:
        return 'cd'

    if number < 900:
        return 'cd' + int_to_mini_roman(number - 400)

    if number == 900:
        return 'cm'

    if number < 1000:
        return 'cm' + int_to_mini_roman(number - 900)
