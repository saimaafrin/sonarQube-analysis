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
        raise ValueError("Invalid input")

    map_thresholds = {
        100: "c",
        10: "x",
        1: "i",
    }

    roman_numerals = []
    for threshold, roman_numeral in map_thresholds.items():
        while number >= threshold:
            roman_numerals.append(roman_numeral)
            number -= threshold

    return "".join(roman_numerals)
