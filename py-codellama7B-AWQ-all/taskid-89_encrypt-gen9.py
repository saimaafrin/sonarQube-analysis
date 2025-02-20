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

    encrypted_str = ''
    for letter in s:
        if letter.isupper():
            encrypted_str += chr((ord(letter) - ord('A') + 26 * 2) % 26 + ord('A'))
        else:
            encrypted_str += chr((ord(letter) - ord('a') + 26 * 2) % 26 + ord('a'))
    return encrypted_str
