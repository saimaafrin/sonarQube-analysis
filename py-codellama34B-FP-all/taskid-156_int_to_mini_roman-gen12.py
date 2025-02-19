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

    if number == 0:
        raise ValueError('Invalid input')
    # Conversion table to map number to roman numerals.
    conversion_table = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    # Find the highest base value in the conversion table that is less than the number.
    # We will use this base to determine the correct roman numerals.
    base = 1
    while base in conversion_table and base < number:
        base *= 10
    # Divide the number by the base to get the number of times to repeat the roman numerals.
    num_repeats = number // base
    # Find the appropriate roman numerals to repeat.
    roman_numeral = ''
    while num_repeats:
        roman_numeral += conversion_table[base]
        num_repeats -= 1
    # If the number is a multiple of the base, we don't need to append any remaining roman numerals.
    # Otherwise, we need to find the difference between the number and the base.
    if number % base:
        # Find the appropriate roman numerals to append.
        roman_numeral += conversion_table[number % base]
    return roman_numeral
