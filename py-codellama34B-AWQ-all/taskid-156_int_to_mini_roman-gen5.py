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


    def int_to_roman(number: int) -> str:
        """
        Given a positive integer, obtain its roman numeral equivalent as a string,
        and return it in lowercase.
        Restrictions: 1 <= num <= 5000

        Examples:
        >>> int_to_roman(19)
        'xix'
        >>> int_to_roman(152)
        'clxii'
        >>> int_to_roman(426)
        'cdxxvi'
        """
        # Credit: https://www.geeksforgeeks.org/converting-decimal-number-
        #  roman-numerals/
        roman_numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman = ""

        for value, numeral in roman_numerals:
            while number >= value:
                roman += numeral
                number -= value

        return roman

    return int_to_roman(number).lower()
