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

    # Use a dict to map the roman numeral symbols to the corresponding
    # arabic number values.
    roman_numeral_map = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i"
    }

    result = ""

    # Use a loop to iterate through the keys of the roman_numeral_map.
    # Compare the value of each key to the number parameter, and if it
    # is equal, concatenate the corresponding value of the key to the
    # result.
    for key in sorted(roman_numeral_map.keys(), reverse=True):
        while number >= key:
            result += roman_numeral_map[key]
            number -= key

    # Return the resulting string.
    return result
