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
    elif string == ' ':
        return False
    else:
        i = 0
        while i < len(string):
            if string.count(string[i]) > 1:
                return False
            i += 1
        return True
