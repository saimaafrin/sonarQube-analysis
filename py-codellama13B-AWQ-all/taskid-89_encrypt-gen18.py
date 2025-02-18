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

    cipher_text = ''
    for char in s:
        if char.isalpha():
            index = ord(char) - ord('a') + 2
            cipher_text += chr(ord('a') + (index % 26))
        else:
            cipher_text += char
    return cipher_text
