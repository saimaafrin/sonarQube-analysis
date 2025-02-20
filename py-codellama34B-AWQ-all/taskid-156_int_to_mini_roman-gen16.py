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


    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Please enter a positive integer from 1 to 1000")
    if number < 10:
        return _convert_ones(number)
    if number < 100:
        return _convert_tens(number)
    if number < 1000:
        return _convert_hundreds(number)
