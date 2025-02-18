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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in s:
        index = alphabet.index(char)
        if index != -1:
            encrypted += alphabet[index+2*2]
        else:
            encrypted += char
    return encrypted
