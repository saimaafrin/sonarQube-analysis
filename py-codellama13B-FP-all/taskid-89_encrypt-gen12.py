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

    # Replace this line with your code
    result = ''
    for letter in s:
        if letter.isalpha():
            shift = (ord(letter) - ord('a') + 2) % 26
            result += chr(ord('a') + shift)
        else:
            result += letter
    return result

    # Don't modify this line
    return encrypt
