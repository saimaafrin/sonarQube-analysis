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


    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Please provide a positive integer within [1, 1000]")

    # Initialize the roman numeral representation
    roman_num = ""

    # Create a list of tuples of the form (roman_repr, value)
    # This is to handle the edge case when there are multiple
    # roman numerals for a given integer
    # Eg. 152 -> 'clii' and not 'clxxii'
    roman_values = [
        ("m", 1000),
        ("d", 500),
        ("c", 100),
        ("l", 50),
        ("x", 10),
        ("v", 5),
        ("i", 1),
    ]

    # Iterate over the list of tuples and append the roman
    # numerals to the string
    for roman, value in roman_values:

        # Calculate the quotient and remainder
        quotient, remainder = divmod(number, value)

        # If the quotient is greater than 0, append the roman numeral
        # to the string the required number of times
        if quotient > 0:
            roman_num += roman * quotient

        # Update the number to be the remainder
        number = remainder

    return roman_num
