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

    number = int(number)
    # Roman numeral has 1000, 500, 100, 50, 10, 5, 1.
    thousands = [
        ["", "m", "mm", "mmm"],
        ["", "d", "dd", "ddd"],
        ["", "c", "cc", "ccc"],
        ["", "l", "ll", "lll"],
        ["", "x", "xx", "xxx"],
        ["", "v", "vv", "vvv"],
        ["", "i", "ii", "iii"],
    ]
    return "".join(thousands[i][number % 1000 // 10 ** i]
                   for i in range(len(thousands)))
