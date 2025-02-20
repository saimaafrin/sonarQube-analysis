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
        raise ValueError(
            f"Invalid input.  Expected a positive integer in the range 1-1000, but got {number}."
        )

    roman_numerals = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1),
    ]
    res = []
    for numeral, value in roman_numerals:
        while number >= value:
            res.append(numeral)
            number -= value

    return "".join(res)
