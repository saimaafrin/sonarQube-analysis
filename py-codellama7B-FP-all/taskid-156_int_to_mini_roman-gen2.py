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


    # Roman numerals have a pattern to their numbers, so we can do this with
    # a series of if/else statements.
    roman_num = ""

    if number == 1000:
        return "m"
    elif number == 900:
        return "cm"
    elif number == 500:
        return "d"
    elif number == 400:
        return "cd"
    elif number == 100:
        return "c"
    elif number == 90:
        return "xc"
    elif number == 50:
        return "l"
    elif number == 40:
        return "xl"
    elif number == 10:
        return "x"
    elif number == 9:
        return "ix"
    elif number == 5:
        return "v"
    elif number == 4:
        return "iv"
    elif number == 1:
        return "i"
    else:
        raise ValueError("The given number is not in range!")

    return roman_num
