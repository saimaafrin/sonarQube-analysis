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

    number = int(number)
    assert 1 <= number <= 1000

    roman_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman_str = ''

    for digit in range(1, 4):
        if number < 4:
            roman_str = roman_map[10**(digit-1)]*number + roman_str
            break
        elif number < 9:
            roman_str = roman_map[10**(digit-1)] + roman_map[5*10**(digit-1)] + roman_str
            break
        elif number < 40:
            roman_str = roman_map[10**(digit-1)]*5 + roman_str
            number -= 5
        elif number < 90:
            roman_str = roman_map[10**(digit-1)]*9 + roman_str
            break
        elif number < 400:
            roman_str = roman_map[10**(digit-1)]*5 + roman_map[10**(digit-1)] + roman_str
            number -= 9
        elif number < 900:
            roman_str = roman_map[10**(digit-1)]*1 + roman_map[5*10**(digit-1)] + roman_str
            number -= 99
        else:
            roman_str = roman_map[10**(digit-1)]*1 + roman_map[10**(digit-1)]*9 + roman_str
            number -= 999

    return roman_str
