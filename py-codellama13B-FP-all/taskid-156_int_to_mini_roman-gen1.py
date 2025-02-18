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

    # Step 1:
    # Convert the given integer to a list of base-10 digits, and reverse it.
    # This list will be used to iterate over the number's digits, from right to left.
    reversed_list = list(str(number))[::-1]

    # Step 2:
    # Define a list to hold the result. It will contain the base-10 digits of the number,
    # represented by their roman numeral equivalent.
    roman_numeral_list = []

    # Step 3:
    # Iterate over the list of digits, from right to left.
    # For each digit,
    # - If the digit is a 0, append a "nulla" to the result list.
    # - Otherwise, append the roman numeral equivalent of the digit to the result list.
    for digit in reversed_list:
        if int(digit) == 0:
            roman_numeral_list.append("nulla")
        elif int(digit) == 1:
            roman_numeral_list.append("i")
        elif int(digit) == 2:
            roman_numeral_list.append("ii")
        elif int(digit) == 3:
            roman_numeral_list.append("iii")
        elif int(digit) == 4:
            roman_numeral_list.append("iv")
        elif int(digit) == 5:
            roman_numeral_list.append("v")
        elif int(digit) == 6:
            roman_numeral_list.append("vi")
        elif int(digit) == 7:
            roman_numeral_list.append("vii")
        elif int(digit) == 8:
            roman_numeral_list.append("viii")
        elif int(digit) == 9:
            roman_numeral_list.append("ix")

    # Step 4:
    # Join the result list into a string, and return it.
    # The digits will be separated by spaces.
    result = " ".join(roman_numeral_list)
    return result
