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


    # Define the symbols which will be used for the conversion
    # Define the mapping of symbols to their values
    symbol_map = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }

    # Define the mapping of symbols to their symbols which precede them
    symbol_precedence = {
        'i': 'v',
        'v': 'x',
        'x': 'l',
        'l': 'c',
        'c': 'd',
        'd': 'm'
    }

    # Define a mapping of symbols to their symbols which follow them
    symbol_following = {
        'v': 'i',
        'x': 'v',
        'l': 'x',
        'c': 'l',
        'd': 'c',
        'm': 'd'
    }

    # Define a function to determine whether the second symbol
    # is one which precedes the first symbol
    def precedes(first: str, second: str) -> bool:
        return symbol_map[second] == symbol_map[symbol_precedence[first]]

    # Define a function to determine whether the first symbol
    # is one which is followed by the second symbol
    def follows(first: str, second: str) -> bool:
        return symbol_map[first] == symbol_map[symbol_following[second]]

    # Define a function to determine the number of times
    # a symbol may be repeated in a row
    def max_repeats(symbol: str) -> int:
        return int(symbol_map[symbol] / symbol_map[symbol_precedence[symbol]])

    # Initialize the output string
    roman_numeral = ''

    # Create a copy of the number
    number_copy = number

    # While the number is non-zero, loop
    while number_copy > 0:

        # Determine the maximum number of times the current symbol may be repeated
        max_count = min(max_repeats(roman_numeral[-1]), number_copy)

        # Determine whether the symbol may be repeated at all
        may_repeat = precedes(roman_numeral[-1], roman_numeral[-2])

        # If the symbol may be repeated, repeat it the maximum number of times
        if may_repeat and max_count > 0:
            roman_numeral += roman_numeral[-1] * max_count

        # Subtract the number of times the symbol was repeated
        number_copy -= symbol_map[roman_numeral[-1]] * max_count

        # If the symbol may not be repeated, replace it with a symbol which follows it
        if not may_repeat and number_copy > 0:
            roman_numeral += symbol_following[roman_numeral[-1]]
            number_copy -= symbol_map[symbol_following[roman_numeral[-2]]]

    # Return the roman numeral
    return roman_numeral
