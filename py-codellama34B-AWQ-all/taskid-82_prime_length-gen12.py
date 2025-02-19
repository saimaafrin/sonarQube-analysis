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

    # get the string length
    length = len(string)

    # check if the length is a prime number
    if length == 2:
        return True
    if length == 1 or length % 2 == 0:
        return False

    # for all other odd numbers, try dividing by all the odd numbers up to the
    # square root of the length. if we get any factors, return False
    for i in range(3, int(length ** 0.5) + 1, 2):
        if length % i == 0:
            return False

    return True
