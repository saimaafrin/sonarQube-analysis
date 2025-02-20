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

    roman = ""
    number = int(number)

    def get_next_val(i: int) -> int:
        return (
            (2 ** i)
            if number >= (2 ** i)
            else (2 ** (i - 1))
            if number >= (2 ** (i - 1))
            else (2 ** (i - 2))
            if number >= (2 ** (i - 2))
            else 0
        )

    def get_next_char(i: int) -> str:
        return {
            (2 ** i): "m",
            (2 ** (i - 1)): "c",
            (2 ** (i - 2)): "x",
            (2 ** (i - 3)): "i",
            (2 ** (i - 4)): "v",
            (2 ** (i - 5)): "i",
        }[get_next_val(i)]

    for i in range(13, 0, -1):
        while number >= get_next_val(i):
            number -= get_next_val(i)
            roman += get_next_char(i)

    return roman
