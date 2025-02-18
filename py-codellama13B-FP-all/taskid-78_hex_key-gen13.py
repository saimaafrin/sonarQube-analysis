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

    # 1. define prime numbers and the list of hexadecimal digits
    prime_numbers = [2, 3, 5, 7, 11, 13, 17]
    hex_numbers = '0123456789ABCDEF'

    # 2. convert the input string into the list of hexadecimal digits
    hex_digits = [num[i] for i in range(len(num))]

    # 3. count the number of primes in the input string
    count = 0
    for digit in hex_digits:
        # 3.1 convert the hexadecimal digit into decimal number
        decimal_digit = int(hex_numbers.index(digit))

        # 3.2 check if the decimal digit is a prime number
        if decimal_digit in prime_numbers:
            count += 1

    return count
