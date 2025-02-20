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


    if string == '':
        return False

    if string == ' ':
        return False

    length = len(string)

    if length == 1:
        return False

    for x in range(2, length - 1):
        if length % x == 0:
            return False

    return True
