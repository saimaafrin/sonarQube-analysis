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

    encryptor = "abcdefghijklmnopqrstuvwxyz"
    decryptor = "zxwvutsrqponmlkjihgfedcba"
    encrypted = ""
    for i in s:
        for j in range(2):
            encrypted += decryptor[encryptor.index(i)]
    return encrypted
