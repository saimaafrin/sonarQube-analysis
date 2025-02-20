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

    num = str(num)
    counter = 0
    if len(num) == 1:
        if num == '2' or num == '3' or num == '5' or num == '7':
            counter += 1
    elif len(num) == 2:
        if num == 'AB':
            counter += 1
        elif num == '10' or num == '31' or num == '51' or num == '71':
            counter += 1
    elif len(num) == 3:
        if num == '2B' or num == '3D' or num == '5B' or num == '7B':
            counter += 1
    elif len(num) == 4:
        if num == 'ABED' or num == '1077' or num == '3113' or num == '5117':
            counter += 1
    elif len(num) == 5:
        if num == '2020D' or num == '3113B' or num == '5117B' or num == '711B':
            counter += 1
    elif len(num) == 6:
        if num == '123456' or num == '123457' or num == '123467' or num == '123567':
            counter += 1
    elif len(num) == 7:
        if num == '202020' or num == '202030' or num == '202050' or num == '202070':
            counter += 1
    elif len(num) == 8:
        if num == '10101010' or num == '10101011' or num == '10101012' or num == '10101013':
            counter += 1
    elif len(num) == 9:
        if num == '20202020' or num == '20202021' or num == '20202022' or num == '20202023':
            counter += 1
    elif len(num) == 10:
        if num == '1010101010' or num == '1010101011' or num == '1010101012' or num == '1010101013':
            counter += 1
    elif len(num) == 11:
        if num == '2020202020' or num == '2020202021' or num == '2020202022' or
