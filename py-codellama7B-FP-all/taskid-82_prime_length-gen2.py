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

    # Your code here
    num = 0
    for i in range(1, len(string) + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            num += 1
    if num == 1:
        return True
    return False
