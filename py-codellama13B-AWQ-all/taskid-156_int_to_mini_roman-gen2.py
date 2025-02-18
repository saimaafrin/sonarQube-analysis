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

    # initialize the empty string that we will fill with the roman numeral
    # equivalent of the input number
    result = ""

    # initialize a dictionary that will map each digit of the input number to its
    # corresponding roman numeral character
    digit_to_roman = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m"
    }

    # loop through the digits of the input number, from least significant to
    # most significant
    for index in range(1, 5):
        # extract the digit of the input number corresponding to the current
        # iteration of the loop
        current_digit = number // (10 ** index)

        # extract the roman numeral character corresponding to the current
        # digit
        current_roman_numeral = digit_to_roman[current_digit]

        # fill the empty string with the current roman numeral character as many
        # times as the current digit is
        result += current_roman_numeral * current_digit

    # return the filled empty string as the roman numeral equivalent of the input
    # number
    return result.lower()
