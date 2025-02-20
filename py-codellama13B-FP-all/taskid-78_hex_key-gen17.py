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

    # +++your code here+++
    # Define the dictionary of hexadecimal digits and their corresponding
    # prime or composite status
    hex_digits = {
        '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,
        '8': 0, '9': 0, 'A': 0, 'B': 1, 'C': 0, 'D': 1, 'E': 0, 'F': 0
    }
    
    # Initialize an empty list to store the number of prime hexadecimal digits
    prime_count = 0
    
    # Iterate through each character in the input string
    for char in num:
        # If the character is a hexadecimal digit and it is prime, add 1 to the count
        if hex_digits[char] == 1:
            prime_count += 1
    
    # Return the count of prime hexadecimal digits
    return prime_count
