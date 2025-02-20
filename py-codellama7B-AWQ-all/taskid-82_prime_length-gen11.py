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

    return len(string) > 0 and len(string) % 2 == 1 and all(map(lambda x: x, (len(string) % i == 0 for i in range(2, len(string)))))
