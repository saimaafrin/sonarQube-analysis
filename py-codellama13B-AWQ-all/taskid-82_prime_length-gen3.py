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

    if len(string) == 0:
        return False
    else:
        for i in range(2, int(len(string) ** 0.5) + 1):
            if len(string) % i == 0:
                return False
        return True
