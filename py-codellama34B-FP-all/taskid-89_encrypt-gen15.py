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

    result = ''
    for char in s:
        if char.isalpha():
            shifted = ord(char) + 2 ** 2
            if char.islower():
                if shifted > ord('z'):
                    result += chr(ord('a') + shifted - ord('z') - 1)
                else:
                    result += chr(shifted)
            else:
                if shifted > ord('Z'):
                    result += chr(ord('A') + shifted - ord('Z') - 1)
                else:
                    result += chr(shifted)
        else:
            result += char
    return result
