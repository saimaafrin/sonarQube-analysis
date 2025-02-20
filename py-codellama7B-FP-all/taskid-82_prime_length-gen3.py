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


    is_prime = False
    prime_list = []
    for i in range(2, string.__len__() + 1):
        if i % 2 != 0:
            if i == 3:
                prime_list.append(i)
            elif i > 3:
                for j in range(3, int(i ** 0.5) + 1, 2):
                    if i % j == 0:
                        break
                else:
                    prime_list.append(i)
    for i in range(0, prime_list.__len__()):
        if prime_list[i] == string.__len__():
            is_prime = True
    return is_prime
