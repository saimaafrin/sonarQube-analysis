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

    roman_dict = {
        1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'
    }
    roman_numeral = ''
    if number == 0:
        raise ValueError("Roman numerals don't have a zero value.")

    if number < 1:
        raise ValueError(f'The number {number} is too small to be expressed as a Roman numeral.')

    if number > 1000:
        raise ValueError(f'The number {number} is too big to be expressed as a Roman numeral.')

    # the algorithm
    digit_list = [int(digit) for digit in str(number)]
    if len(digit_list) == 4:
        roman_numeral = roman_numeral + roman_dict[1000] * digit_list.pop(0)

    if len(digit_list) == 3:
        roman_numeral = roman_numeral + roman_dict[100] * digit_list.pop(0)

    if len(digit_list) == 2:
        tens = digit_list.pop(0)
        if 0 < tens < 4:
            roman_numeral = roman_numeral + roman_dict[10] * tens
        elif tens == 4:
            roman_numeral = roman_numeral + roman_dict[5] + roman_dict[10]
        else:
            roman_numeral = roman_numeral + roman_dict[5] + roman_dict[10] * (tens - 5)

    if len(digit_list) == 1:
        ones = digit_list.pop(0)
        if 0 < ones < 4:
            roman_numeral = roman_numeral + roman_dict[1] * ones
        elif ones == 4:
            roman_numeral = roman_numeral + roman_dict[5] + roman_dict[1]
        else:
            roman_numeral = roman_numeral + roman_dict[5] + roman_dict[1] * (ones - 5)

    return roman_numeral
