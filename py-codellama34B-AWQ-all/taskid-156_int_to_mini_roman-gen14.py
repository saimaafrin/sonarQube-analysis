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
        raise ValueError(f"Input must be between 1 and 1000 inclusive")

    roman_numeral_map = [
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
    ]

    result = []
    while number > 0:
        for num_value, roman_char in roman_numeral_map:
            if number >= num_value:
                number -= num_value
                result.append(roman_char)
                break

    return "".join(result)
