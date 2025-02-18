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

    roman = ''
    # Iterate over the 10^i, where i = 0, 1, ..., 6, to process 10**7.
    for i in range(7):
        num_to_process = number // 10**i
        number -= num_to_process * 10**i

        if num_to_process != 0:
            if num_to_process < 4:
                roman += ''.join(list(map(lambda x: num_to_process * x,
                                           mini_roman[1:])))
            else:
                roman += mini_roman[num_to_process - 5]

    return roman
