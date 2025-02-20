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

    if not 1 <= number <= 1000:
        raise ValueError(f"'{number}' is out of range")
    numerals = [("i", 1), ("v", 5), ("x", 10), ("l", 50), ("c", 100), ("d", 500), ("m", 1000)]
    result = ""
    while number > 0:
        for numeral, value in numerals:
            if number < value:
                continue
            result += numeral * (number // value)
            number %= value
    return result
