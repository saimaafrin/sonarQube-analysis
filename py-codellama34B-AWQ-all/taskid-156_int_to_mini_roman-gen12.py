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
        raise ValueError(f"Integer must be within range [1, 1000], got {number}")

    roman_numeral_map = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm',
    }

    # Divide the number by 10**n for n in [0, 3] to get its digit at that position.
    # Then look up the digit to find its roman numeral.
    # Iterate in reverse order to build the roman numeral from left to right.
    roman_numeral = ''
    for power in reversed(range(0, 4)):
        digit = (number // 10**power) % 10
        roman_numeral = roman_numeral_map[digit * 10**power] + roman_numeral

    return roman_numeral
