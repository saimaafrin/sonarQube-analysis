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


    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    return is_prime(len(string))
