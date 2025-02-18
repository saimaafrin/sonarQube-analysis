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

    if num == "":
        return 0
    hex_list = []
    hex_list.append(0)
    hex_list.append(1)
    hex_list.append(2)
    hex_list.append(3)
    hex_list.append(4)
    hex_list.append(5)
    hex_list.append(6)
    hex_list.append(7)
    hex_list.append(8)
    hex_list.append(9)
    hex_list.append(10)
    hex_list.append(11)
    hex_list.append(12)
    hex_list.append(13)
    hex_list.append(14)
    hex_list.append(15)
    prime_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    prime_hex = []
    for n in prime_num:
        hex_num = hex(n)[2:].upper()
        prime_hex.append(hex_num)
    count = 0
    for i in num:
        if i in prime_hex:
            count += 1
    return count
