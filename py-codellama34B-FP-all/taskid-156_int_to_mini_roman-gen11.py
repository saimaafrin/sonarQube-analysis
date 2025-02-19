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
        raise ValueError(f"The number {number} is outside the range [1, 1000].")

    # The following is a dictionary that contains the numbers from 1 to 1000.
    # The key is the number, the value is its roman numeral in lowercase.
    #
    # The numbers are organized in such a way that they are grouped by the digit
    # that changes in the roman numeral.
    # For example:
    #   10, 20, 30, 40, 50, 60, 70, 80, 90 are grouped together because
    #   their tens place change.
    #
    #   Similarly, 1, 2, 3, 4, 5, 6, 7, 8, 9 are grouped together because their
    #   ones place change.
    #
    # If you look at the pattern for the hundreds place, it's similar.
    # So we can use a pattern to extract the number in the thousands place,
    # the hundreds place, the tens place and the ones place, and then we can
    # find their roman numeral equivalents from this dictionary.
    roman_numerals = {
        1: 'i',
        2: 'ii',
        3: 'iii',
        4: 'iv',
        5: 'v',
        6: 'vi',
        7: 'vii',
        8: 'viii',
        9: 'ix',
        10: 'x',
        20: 'xx',
        30: 'xxx',
        40: 'xl',
        50: 'l',
        60: 'lx',
        70: 'lxx',
        80: 'lxxx',
        90: 'xc',
        100: 'c',
        200: 'cc',
        300: 'ccc',
        400: 'cd',
        500: 'd',
        600: 'dc',
        700: 'dcc',
        800: 'dccc',
        900: 'cm',
        1000: 'm'
    }

    # This pattern will help us extract the digits from the number.
    # The first digit is the ones place.
    # The second digit is the tens place.
    # The third digit is the hundreds place.
    # The fourth digit is the thousands place.
    digit_pattern = '%04d'

    # Format the number into the pattern.
    # E.g. 1921 -> 01921
    number_string = digit_pattern % number

    # The ones place is the last digit.
    ones_digit = int(number_string[-1])

    # The tens place is the second to last digit.
    tens_digit = int(number_string[-2])

    # The hundreds place is the third to last digit.
    hundreds_digit = int(number_string[-3])

    # The thousands place is the fourth to last digit.
    thousands_digit = int(number_string[-4])

    # Obtain the roman numeral of each digit.
    ones_roman = roman_numerals[ones_digit]
    tens_roman = roman_numerals[tens_digit * 10]
    hundreds_roman = roman_numerals[hundreds_digit * 100]
    thousands_roman = roman_numerals[thousands_digit * 1000]

    return thousands_roman + hundreds_roman + tens_roman + ones_rom
