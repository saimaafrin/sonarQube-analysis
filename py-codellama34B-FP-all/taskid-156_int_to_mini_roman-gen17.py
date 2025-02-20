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

    # Convert the integer into a string
    number = str(number)

    # Define a dictionary of Roman numerals and their values
    roman_numerals = {
        '1': 'i',
        '2': 'ii',
        '3': 'iii',
        '4': 'iv',
        '5': 'v',
        '6': 'vi',
        '7': 'vii',
        '8': 'viii',
        '9': 'ix',
        '10': 'x',
        '20': 'xx',
        '30': 'xxx',
        '40': 'xl',
        '50': 'l',
        '60': 'lx',
        '70': 'lxx',
        '80': 'lxxx',
        '90': 'xc',
        '100': 'c',
        '200': 'cc',
        '300': 'ccc',
        '400': 'cd',
        '500': 'd',
        '600': 'dc',
        '700': 'dcc',
        '800': 'dccc',
        '900': 'cm',
        '1000': 'm',
    }

    # Define a dictionary of Roman numerals and their values
    special_roman_numerals = {
        '51': 'li',
        '52': 'lii',
        '53': 'liii',
        '54': 'liv',
        '56': 'lvi',
        '57': 'lvii',
        '58': 'lviii',
        '59': 'lix',
        '41': 'xlvi',
        '42': 'xlvii',
        '43': 'xlviii',
        '44': 'xlix',
        '45': 'xlv',
        '46': 'xlvi',
        '47': 'xlvii',
        '48': 'xlviii',
        '49': 'xlix',
        '91': 'xci',
        '92': 'xcii',
        '93': 'xciii',
        '94': 'xciv',
        '96': 'xcvi',
        '97': 'xcvii',
        '98': 'xcviii',
        '99': 'xcix',
        '400': 'cd',
        '900': 'cm',
    }

    # Loop through the string of the integer
    for key in special_roman_numerals:
        if key in number:
            number = number.replace(key, special_roman_numerals[key])

    # Loop through the string of the integer
    for key in roman_numerals:
        if key in number:
            number = number.replace(key, roman_numerals[key])

    # Return the Roman numeral equivalent of the integer
    return number.lower()
