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

    return any(string[i:i + x] == string[i + x:i + x * 2] for x in range(1, len(string)) for i in range(len(string) - x * 2 + 1))
