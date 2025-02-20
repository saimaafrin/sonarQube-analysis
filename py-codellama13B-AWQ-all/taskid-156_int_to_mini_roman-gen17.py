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

    if number == 0:
        raise ValueError("Input must be a positive integer")
    if number > 1000:
        raise ValueError("Input must be less than or equal to 1000")

    roman = ""

    # Handle the hundreds digit
    hundreds = number // 100
    if hundreds == 9:
        roman += "cm"
    elif hundreds == 4:
        roman += "cd"
    else:
        roman += int_to_mini_roman(hundreds)
        roman += "c"

    # Handle the tens digit
    number = number % 100
    tens = number // 10
    if tens == 9:
        roman += "xc"
    elif tens == 4:
        roman += "xl"
    else:
        roman += int_to_mini_roman(tens)
        roman += "x"

    # Handle the ones digit
    ones = number % 10
    if ones == 9:
        roman += "ix"
    elif ones == 4:
        roman += "iv"
    else:
        roman += int_to_mini_roman(ones)
        roman += "i"

    return roman.lower()
