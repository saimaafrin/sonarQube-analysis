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

    #TODO: implement the function
    if len(string) == 0:
        return False
    if len(string) == 1:
        return False
    if len(string) == 2:
        return False
    is_prime = False
    for i in range(2, len(string)):
        if len(string) % i == 0:
            is_prime = True
    return is_prime
