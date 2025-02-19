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

    result = ""
    # The only symbols we need are: I, V, X, L, C, D, M
    # We'll start with the largest symbols, and work our way down
    # We can just subtract the smallest symbol from the number
    # if it is larger than that symbol, and add the symbol
    # to the result string

    while number > 0:
        # If the number is greater than 1000, just subtract 1000
        # and add the symbol 'm' to the result
        if number >= 1000:
            number -= 1000
            result += "m"

        # If the number is greater than 900, subtract 900 and add
        # the symbol 'cm' to the result
        elif number >= 900:
            number -= 900
            result += "cm"

        # If the number is greater than 500, subtract 500 and add
        # the symbol 'd' to the result
        elif number >= 500:
            number -= 500
            result += "d"

        # If the number is greater than 400, subtract 400 and add
        # the symbol 'cd' to the result
        elif number >= 400:
            number -= 400
            result += "cd"

        # If the number is greater than 100, subtract 100 and add
        # the symbol 'c' to the result
        elif number >= 100:
            number -= 100
            result += "c"

        # If the number is greater than 90, subtract 90 and add
        # the symbol 'xc' to the result
        elif number >= 90:
            number -= 90
            result += "xc"

        # If the number is greater than 50, subtract 50 and add
        # the symbol 'l' to the result
        elif number >= 50:
            number -= 50
            result += "l"

        # If the number is greater than 40, subtract 40 and add
        # the symbol 'xl' to the result
        elif number >= 40:
            number -= 40
            result += "xl"

        # If the number is greater than 10, subtract 10 and add
        # the symbol 'x' to the result
        elif number >= 10:
            number -= 10
            result += "x"

        # If the number is greater than 9, subtract 9 and add
        # the symbol 'ix' to the result
        elif number >= 9:
            number -= 9
            result += "ix"

        # If the number is greater than 5, subtract 5 and add
        # the symbol 'v' to the result
        elif number >= 5:
            number -= 5
            result += "v"

        # If the number is greater than 4, subtract 4 and add
        # the symbol 'iv' to the result
        elif number >= 4:
            number -= 4
            result += "iv"

        # If the number is greater than 1, subtract 1 and add
        # the symbol 'i' to the result
        elif number >= 1:
            number -= 1
            result += "i"

    return result
