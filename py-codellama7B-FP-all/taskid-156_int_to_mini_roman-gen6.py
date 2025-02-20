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

    # Mapping roman numerals to integers
    # (The mapping of the digits in reverse order is what we need)
    roman_dict = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }
    # The mapping of the roman numerals to the digits in reverse order
    roman_to_num_dict = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }
    # Initialize the list to store the roman numerals
    roman_num_list = []
    # Iterate until the number becomes 0
    while number > 0:
        # If the number is greater than the corresponding roman numeral
        # (e.g. 9 > X), we append the roman numeral to the list
        if number >= roman_dict['M']:
            roman_num_list.append('M')
            number -= roman_dict['M']
        elif number >= roman_dict['D']:
            roman_num_list.append('D')
            number -= roman_dict['D']
        elif number >= roman_dict['C']:
            roman_num_list.append('C')
            number -= roman_dict['C']
        elif number >= roman_dict['L']:
            roman_num_list.append('L')
            number -= roman_dict['L']
        elif number >= roman_dict['X']:
            roman_num_list.append('X')
            number -= roman_dict['X']
        elif number >= roman_dict['V']:
            roman_num_list.append('V')
            number -= roman_dict['V']
        elif number >= roman_dict['I']:
            roman_num_list.append('I')
            number -= roman_dict['I']
    # Join the roman numerals to form the final string
    return ''.join(roman_num_list)
