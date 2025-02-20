def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # Convert to a string
    digits = str(x)
    # Create the empty string to store the circularly shifted digits
    circular_shifted_string = ''

    # Get the number of digits in x
    num_digits = len(digits)

    # Check if the shift is greater than the number of digits
    if shift > num_digits:
        # If so, return the digits reversed
        return digits[::-1]

    # Circularly shift the digits to the right by shift
    for i in range(num_digits - shift):
        # Add the current digit to the circularly shifted string
        circular_shifted_string += digits[i]

    # Add the last shift digits to the circularly shifted string
    for i in range(num_digits - shift, num_digits):
        circular_shifted_string += digits[i]

    return circular_shifted_string
