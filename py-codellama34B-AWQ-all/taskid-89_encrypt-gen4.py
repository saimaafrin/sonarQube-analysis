def encrypt(s: str) -> str:
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """

    # your code here
    encrypt = ''
    for letter in s:
        num = ord(letter)
        if num >= 97 and num <= 109:
            num += 13
        elif num >= 100 and num <= 113:
            num -= 13
        encrypt += chr(num)
    return encrypt
