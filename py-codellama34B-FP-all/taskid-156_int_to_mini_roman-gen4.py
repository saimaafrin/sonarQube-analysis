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

    if number > 1000 or number <= 0:
        raise ValueError("The value provided should be between 1 and 1000, inclusive.")
    if number == 1000:
        return "m"
    if number < 100:
        return _convert_tens(number)
    if number < 1000:
        return _convert_hundreds(number)
    raise NotImplementedError("This method doesn't handle numbers greater than 1000.")
