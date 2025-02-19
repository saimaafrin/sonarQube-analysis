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

    encrypted_string = ''
    for letter in s:
        if 'a' <= letter <= 'z':
            new_ord = ord(letter) + 2 * 2
            if new_ord > ord('z'):
                new_ord -= 26
            encrypted_string += chr(new_ord)
        elif 'A' <= letter <= 'Z':
            new_ord = ord(letter) + 2 * 2
            if new_ord > ord('Z'):
                new_ord -= 26
            encrypted_string += chr(new_ord)
        else:
            encrypted_string += letter
    return encrypted_string
