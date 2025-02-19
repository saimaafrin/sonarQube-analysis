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


    def is_prime(n: int) -> bool:
        if n <= 1 or n % 2 == 0 and n > 2:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def hex_digit_to_int(digit: str) -> int:
        if digit.isdigit():
            return int(digit)
        return '0123456789ABCDEF'.index(digit)

    return sum(is_prime(hex_digit_to_int(digit)) for digit in num)
