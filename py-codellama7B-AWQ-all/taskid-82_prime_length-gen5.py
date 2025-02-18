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

    prime_list = []
    for i in range(2, 100):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            prime_list.append(i)
    for i in prime_list:
        if len(string) == i:
            return True
    return False
