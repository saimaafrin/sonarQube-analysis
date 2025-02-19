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


    def to_roman(n: int) -> str:
        """
        Return the corresponding roman numeral as a string.

        Restrictions: 1 <= n <= 1000
        """
        if n <= 0:
            raise ValueError(f'Cannot convert {n} to roman numeral')
        if n > 1000:
            raise ValueError(f'{n} exceeds 1000')

        num_dict = {
            1: 'i',
            5: 'v',
            10: 'x',
            50: 'l',
            100: 'c',
            500: 'd',
            1000: 'm'
        }

        roman_numeral = ''

        if n in num_dict:
            return num_dict[n]

        if n < 5:
            return num_dict[1] * n

        if 5 < n < 10:
            return num_dict[5] + num_dict[1] * (n-5)

        if n == 10:
            return num_dict[10]

        if 10 < n < 50:
            if n % 10 == 0:
                return num_dict[10] + num_dict[1] * (n//10)
            return num_dict[10] + to_roman(n % 10)

        if n == 50:
            return num_dict[50]

        if 50 < n < 100:
            if n % 10 == 0:
                return num_dict[50] + num_dict[10] * (n//10)
            return num_dict[50] + to_roman(n % 10)

        if n == 100:
            return num_dict[100]

        if 100 < n < 500:
            if n % 100 == 0:
                return num_dict[100] + num_dict[10] * (n//100)
            return num_dict[100] + to_roman(n % 100)

        if n == 500:
            return num_dict[500]

        if 500 < n < 1000:
            if n % 100 == 0:
                return num_dict[500] + num_dict[100] * (n//100)
            return num_dict[500] + to_roman(n % 100)

        if n == 1000:
            return num_dict[1000]

    return to_roman(number).lower()
