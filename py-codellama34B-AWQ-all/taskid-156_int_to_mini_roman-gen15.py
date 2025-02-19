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

    if number < 0 or number > 1000:
        raise ValueError("The value of the number is not within the allowed range.")
    # create a dictionary of roman numerals
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    # create an empty string to store the result
    result = ""

    # loop through the dictionary and concatenate the values
    for key, value in roman_numerals.items():
        # get the quotient and the remainder
        quotient = number // value
        remainder = number % value

        # if the quotient is greater than 0, concatenate the key to the result
        if quotient > 0:
            # if the quotient is equal to 4, concatenate the next key to the result
            if quotient == 4:
                result += key + list(roman_numerals.keys())[list(roman_numerals.values()).index(value) + 1]
            # if the quotient is equal to 9, concatenate the next two keys to the result
            elif quotient == 9:
                result += key + list(roman_numerals.keys())[list(roman_numerals.values()).index(value) + 1] + list(
                    roman_numerals.keys())[list(roman_numerals.values()).index(value) + 1]
            # else, concatenate the key to the result, the quotient times
            else:
                result += key * quotient

        # set the number to the remainder
        number = remainder

    return result
