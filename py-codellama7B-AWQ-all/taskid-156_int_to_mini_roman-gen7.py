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

    _1000 = 1000
    _900 = 900
    _500 = 500
    _400 = 400
    _100 = 100
    _90 = 90
    _50 = 50
    _40 = 40
    _10 = 10
    _9 = 9
    _5 = 5
    _4 = 4
    _1 = 1

    def _add_to_roman_numeral(numeral: str, value: int, digit: int) -> str:
        """
        Internal function for converting a digit to a roman numeral.
        """
        if digit == 9:
            return f'{numeral}{value}x'
        elif digit == 4:
            return f'{numeral}{value}x'
        elif digit == 5:
            return f'{numeral}{value}v'
        elif digit == 1:
            return f'{numeral}{value}'
        else:
            raise Exception(f'Invalid digit {digit}')

    def _add_to_roman_numeral_list(roman_numeral: str, number: int) -> str:
        """
        Internal function for converting the number to a roman numeral.
        """
        if number > _1000:
            raise Exception(f'Number {number} is too large')
        elif number == _1000:
            return roman_numeral + 'm'
        elif number >= _900:
            return roman_numeral + _add_to_roman_numeral('', _900, number - _900)
        elif number >= _500:
            return roman_numeral + _add_to_roman_numeral('d', _500, number - _500)
        elif number >= _400:
            return roman_numeral + _add_to_roman_numeral('cm', _400, number - _400)
        elif number >= _100:
            return roman_numeral + _add_to_roman_numeral('c', _100, number - _100)
        elif number >= _90:
            return roman_numeral + _add_to_roman_numeral('xc', _90, number - _90)
        elif number >= _50:
            return roman_numeral + _add_to_roman_numeral('l', _50, number - _50)
        elif number >= _40:
            return roman_numeral + _add_to_roman_numeral('xl', _40, number - _40)
        elif number >= _10:
            return roman_numeral + _add_to_roman_numeral('x', _10, number - _10)
        elif number >= _9:
            return roman_numeral + _add_to_roman_numeral('ix', _9, number - _9)
        elif number >= _5:
            return roman_numeral + _add_to_roman_numeral('v', _5, number - _5)
        elif number >= _4:
            return roman_numeral + _add_to_roman_numeral('iv', _4, number - _4)
        elif number >= _1:
            return roman_numeral + _add_to_roman_numeral('i', _1, number - _1)
        else:
            return roman_numeral

    roman_numeral = ''
    roman_numeral = _add_
