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


    # Dictionary to map each digit to its roman numeral
    # representation.
    roman_numerals_dict = {
        1: "i",
        2: "ii",
        3: "iii",
        4: "iv",
        5: "v",
        6: "vi",
        7: "vii",
        8: "viii",
        9: "ix",
    }

    # Base case: If number is less than or equal to 3, then
    # we need only map it to its equivalent roman numeral.
    if number <= 3:
        return roman_numerals_dict[number]

    # If number is greater than 3, then we can first break
    # it down into its digit equivalent, and then map each
    # digit to its roman numeral equivalent.
    roman_numeral_equivalent = ""
    while number > 0:
        digit = number % 10  # Get the digit equivalent
        number //= 10
        roman_numeral_equivalent = roman_numerals_dict[digit] + roman_numeral_equivalent
    return roman_numeral_equivalent
