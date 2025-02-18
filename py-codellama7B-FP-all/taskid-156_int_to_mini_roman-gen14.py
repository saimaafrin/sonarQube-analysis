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

    # 0 <= num < 4000
    if number <= 0:
        raise ValueError(f'Argument must be positive: {number}')
    # num in [1, 4000)
    # 1 <= num <= 3999
    if number >= 4000:
        raise ValueError(f'Argument too large: {number}')

    # 1 <= num <= 1000
    if number < 1000:
        # 1 <= num <= 999
        return _int_to_mini_roman_helper(number)
    else:
        # 1000 <= num <= 3999
        return (
            _int_to_mini_roman_helper(number // 1000) + 'm' +
            _int_to_mini_roman_helper(number % 1000)
        )
