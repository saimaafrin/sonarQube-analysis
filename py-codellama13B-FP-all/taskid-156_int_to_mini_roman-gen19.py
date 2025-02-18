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

    # We'll use a list for the roman numerals
    roman_numerals = ['m', 'd', 'c', 'l', 'x', 'v', 'i']

    # This will be our output string
    result = ""

    # We'll use a counter to keep track of how many times a digit can be reused
    counter = 0

    # We'll start from the lowest digit (ones) and work our way up
    for digit in range(len(roman_numerals) - 1, -1, -1):
        # Check if this digit is a factor of our input number
        while number % (digit + 1) == 0:
            # If so, use the appropriate roman numeral and decrement the counter
            result += roman_numerals[digit]
            number //= digit + 1
            counter += 1

        # If we've used all possible combinations of this digit, move on to the next one
        if counter == len(roman_numerals) - digit:
            counter = 0

    return result.lower()
