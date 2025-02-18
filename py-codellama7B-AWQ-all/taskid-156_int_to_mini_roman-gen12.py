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

    roman_num: str = ''

    def process_digit(digit: int, prefix: str) -> None:
        roman_num += prefix
        for _ in range(digit):
            roman_num += 'I'

    process_digit(number // 1000, 'm')
    number %= 1000

    process_digit(number // 100, 'c')
    number %= 100

    process_digit(number // 10, 'x')
    number %= 10

    process_digit(number, 'i')

    return roman_num
