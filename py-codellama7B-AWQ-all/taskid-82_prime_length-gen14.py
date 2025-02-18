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

    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    return is_prime(len(string))
