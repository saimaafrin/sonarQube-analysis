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

    if number > 1000:
        raise ValueError("Number cannot be greater than 1000.")
    if number <= 0:
        raise ValueError("Number must be a positive integer.")
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    keys = [
        "i",
        "iv",
        "v",
        "ix",
        "x",
        "xl",
        "l",
        "xci",
        "c",
        "cd",
        "d",
        "cm",
        "m",
    ]
    roman_numeral = ""
    while number > 0:
        for i, val in enumerate(values):
            if number >= val:
                roman_numeral += keys[i]
                number -= val
                break
    return roman_numeral
