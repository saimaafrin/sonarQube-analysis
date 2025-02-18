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

    string = string.lower()
    prime_list = []
    prime_set = set(prime_list)

    for i in string:
        prime_set.add(i)

    for i in prime_set:
        prime_list.append(i)

    prime_string = ''.join(prime_list)
    prime_length = len(prime_string)

    for i in range(2, prime_length + 1):
        if prime_length % i == 0:
            return True
        else:
            return False
