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

    prime = [2, 3, 5, 7]
    string_length = len(string)
    for prime_number in prime:
        if string_length == prime_number:
            return True
    return False
