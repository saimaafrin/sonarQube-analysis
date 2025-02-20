def prime_length(string: str) -> bool:
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    >>> prime_length('Hello')
    True
    >>> prime_length('abcdcba')
    True
    >>> prime_length('kittens')
    True
    >>> prime_length('orange')
    False
    """

    # Check if string is valid
    if not string:
        raise TypeError("Expected string type")

    # Get the length of the string
    length: int = len(string)

    # Loop through all the prime numbers up to the length of the string
    for num in range(2, length + 1):
        # Check if the length of the string is a multiple of the prime number
        if length % num == 0:
            # Length is a multiple of prime number
            return False
    # No multiple of the length of the string found
    return True
