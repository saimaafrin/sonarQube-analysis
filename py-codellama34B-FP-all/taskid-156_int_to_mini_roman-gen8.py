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

    if not (0 < number <= 1000):
        raise ValueError("Must be 1 <= num <= 1000")
    roman_numerals = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }
    roman_num_chars = []
    for val, char in sorted(roman_numerals.items(), reverse=True):
        if number >= val:
            quotient, remainder = divmod(number, val)
            roman_num_chars.append(char * quotient)
            number = remainder

    return "".join(roman_num_chars)
