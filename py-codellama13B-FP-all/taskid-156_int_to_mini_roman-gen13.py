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

    roman_numeral = ''
    tens, digits = divmod(number, 10)
    if tens == 9:
        roman_numeral += 'xc'
    elif tens == 8:
        roman_numeral += 'lxxx'
    elif tens == 7:
        roman_numeral += 'lxx'
    elif tens == 6:
        roman_numeral += 'lx'
    elif tens == 5:
        roman_numeral += 'l'
    elif tens == 4:
        roman_numeral += 'xl'
    elif tens == 3:
        roman_numeral += 'xxx'
    elif tens == 2:
        roman_numeral += 'xx'
    elif tens == 1:
        roman_numeral += 'x'

    if digits == 9:
        roman_numeral += 'ix'
    elif digits == 8:
        roman_numeral += 'viii'
    elif digits == 7:
        roman_numeral += 'vii'
    elif digits == 6:
        roman_numeral += 'vi'
    elif digits == 5:
        roman_numeral += 'v'
    elif digits == 4:
        roman_numeral += 'iv'
    elif digits == 3:
        roman_numeral += 'iii'
    elif digits == 2:
        roman_numeral += 'ii'
    elif digits == 1:
        roman_numeral += 'i'

    return roman_numeral.lower()
