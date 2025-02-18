def hex_key(num: str) -> int:
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    >>> hex_key('AB')
    1
    >>> hex_key('1077E')
    2
    >>> hex_key('ABED1A33')
    4
    >>> hex_key('123456789ABCDEF0')
    6
    >>> hex_key('2020')
    2
    """

    hex_to_dec = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    result = 0
    for x in num:
        if hex_to_dec[x] in [2, 3, 5, 7, 11, 13]:
            result += 1

    return result
