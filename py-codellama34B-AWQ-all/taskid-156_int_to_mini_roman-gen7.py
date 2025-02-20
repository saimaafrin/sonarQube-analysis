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

    # Check if number is a positive integer
    assert isinstance(number, int) and number > 0
    # Create dictionaries for single and group digits
    single_digit = {'1': 'i', '2': 'v', '3': 'x', '4': 'l', '5': 'c', '6': 'd', '7': 'm'}
    double_digit = {'2': 'c', '3': 'x', '4': 'l', '5': 'd', '6': 'm', '7': 'c'}
    # Create an empty string to store the result
    result = ''
    # Loop until number is 0, decrementing number by 1
    while number > 0:
        # Get the last digit of the number
        last_digit = str(number)[-1]
        # If the last digit is 9, add the last digit of the previous single digit to the result
        if last_digit == '9':
            result += single_digit[str(int(last_digit) - 1)]
            number -= 1
            result += single_digit[last_digit]
            number -= 1
        # If the last digit is 4, add the last digit of the previous double digit to the result
        elif last_digit == '4':
            result += double_digit[last_digit]
            number -= 1
            result += single_digit[last_digit]
            number -= 1
        # If the last digit is 5, add the last digit of the previous single digit to the result
        elif last_digit == '5':
            result += single_digit[last_digit]
            number -= 1
        # If the last digit is 6, 7 or 8, add the last digit of the previous single digit to the result
        elif last_digit in ['6', '7', '8']:
            result += single_digit[last_digit]
            number -= 1
            # If the last digit is 6, 7 or 8, add the last digit of the previous single digit to the result
            if last_digit in ['6', '7', '8']:
                result += single_digit[str(int(last_digit) - 1)]
                number -= 1
    return result
