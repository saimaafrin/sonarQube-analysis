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

    #TODO: Implement this function.
    return string.__len__() > 1 and len(list(filter(lambda x: string.__len__() % x == 0, range(2, string.__len__())))) > 0
