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

    # Note: the above examples use the Roman Numeral system with a base of 10
    # where 1 = I, 2 = II, 3 = III, 4 = IV, 5 = V, 6 = VI, 7 = VII, 8 = VIII, 9 = IX
    # 10 = X, etc.

    # Note: The roman numeral system uses the following letters to represent the numbers 5 to 9:
    # V for 5, X for 10, L for 50, C for 100, D for 500, and M for 1000.
    # These letters are used to form the Roman numerals.
    # For example, 4 is written as IV, because it is 5 - 1, and 9 is written as IX, because it is 10 - 1.

    # Given an integer number, return its Roman numeral equivalent.
    # All the numbers will be 1 or 10-1000.

    # Write a function that returns the Roman numeral equivalent of the given integer number.

    # Examples:
    # int_to_roman(1) == "I"
    # int_to_roman(5) == "V"
    # int_to_roman(9) == "IX"
    # int_to_roman(12) == "XII"
    # int_to_roman(16) == "XVI"
    # int_to_roman(20) == "XX"
    # int_to_roman(99) == "XCIX"
    # int_to_roman(100) == "C"
    # int_to_roman(500) == "D"
    # int_to_roman(900) == "CM"
    # int_to_roman(1000) == "M"

    # Hint: the function should return a string.

    # Roman numerals are made up of five symbols: I, V, X, L, and C.

    # The number w written in Roman numerals is:
    # w = 1000*C + 100*D + 10*M + 1*I

    # For example, 2008 is written as "MMVIII" in Roman numerals:
    # 2008 = 1000*C + 100*M + 10*I + 1*I + 1*I + 1*I + 1*I

    # For the Roman numerals to be well-formed, the following rules must be followed:
    # I can only be placed before V (5) and X (10) to make 4 and 9 respectively.
    # X can only be placed before L (50) and C (100) to make 40 and 90 respectively.
    # C can only be placed before D (500) and M (1000) to make 400 and 900 respectively.

    # For example, XXI is written as "XXI" (20 + 1) or XLII is written as "XLII" (40 + 2),
    # because "XXI" (20 + 1) is a more efficient way of writing it.

    # In the same way, I is not written as IIII, because 4 is written as IV.
    # Similarly, X is not written as XXXX, because 20 is written as XC.
    # And so on.

    # If the roman numeral is not well-formed, then return None.
    # For example, "MM
