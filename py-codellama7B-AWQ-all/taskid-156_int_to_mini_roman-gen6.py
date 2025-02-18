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

    def _int_to_mini_roman(number: int) -> str:
        if number == 0:
            return ''
        base = number % 10
        num_str = ''
        if base == 9:
            num_str += 'ix'
            number -= 9
        elif base == 5:
            num_str += 'v'
            number -= 5
        else:
            while base >= 5:
                num_str += 'v'
                base -= 5
        while base >= 1:
            num_str += 'i'
            base -= 1
        return _int_to_mini_roman(number) + num_str

    return _int_to_mini_roman(number)
