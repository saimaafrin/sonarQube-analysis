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

    # roman numerals for each place value
    places = [1000, 100, 10, 1]
    roman_numerals = ['M', 'C', 'X', 'I']
    result = ''
    for i, place in enumerate(places):
        # if place value is non-zero
        if number // place:
            # compute number of letters to add
            count = number // place
            # add roman numeral letter to result
            result += count * roman_numerals[i]
            # subtract place value from number
            number -= count * place
    return result
