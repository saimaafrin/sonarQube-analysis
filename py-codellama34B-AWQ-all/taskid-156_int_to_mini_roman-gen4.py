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

    assert 1 <= number <= 1000

    # Divide the number in 3 parts:
    #   ones
    #   tens
    #   hundreds
    #   thousands
    # We will use a list to store the result, since we don't know
    # in advance the length of the result.

    # We will use a lookup table to map digits to roman numerals.
    # The table is sorted such that the first item corresponds
    # to the units digit, the second to the tens digit, etc.
    lookup = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

    result = []
    num_thousands = number // 1000
    number = number % 1000
    num_hundreds = number // 100
    number = number % 100
    num_tens = number // 10
    num_units = number % 10

    # Add thousands
    for _ in range(num_thousands):
        result.append("m")

    # Add hundreds
    for _ in range(num_hundreds):
        result.append("c")

    # Add tens and units
    result.append(lookup[num_tens])
    result.append(lookup[num_units])

    return "".join(result)
