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
        raise ValueError("Input must be a positive integer <= 1000.")

    roman_numeral = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xlx",
        100: "c",
        400: "cd",
        500: "d",
        900: "xc"
    }

    roman_numeral_str = ""

    for i in range(len(roman_numeral)):
        while number >= roman_numeral[i]:
            roman_numeral_str += roman_numeral[i]
            number -= roman_numeral[i]

    return roman_numeral_str.lower()
