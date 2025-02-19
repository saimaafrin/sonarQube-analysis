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

    if number < 1:
        raise ValueError("Integer must be greater than 0")
    if number > 1000:
        raise ValueError("Integer must be less than or equal to 1000")
    # Create a mapping of numbers to roman numerals
    roman_numerals = [
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
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
    result = ""
    # Iterate through the list and add roman numerals as needed
    for roman_value, roman_numeral in roman_numerals:
        # While the number is greater than the roman value
        while number >= roman_value:
            # Add the roman numeral to the result
            result += roman_numeral
            # Subtract the roman value from the number
            number -= roman_value
    return result
