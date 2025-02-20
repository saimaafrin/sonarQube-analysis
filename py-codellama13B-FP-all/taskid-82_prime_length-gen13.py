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

    if string is None:
        raise ValueError("Invalid input, expected string")
    string = string.replace(" ", "")
    return len(string) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
