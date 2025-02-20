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

    new_string = ""
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            if char.isupper():
                new_ascii = ascii_val + 2
                if new_ascii > 90:
                    new_ascii = new_ascii - 90 + 64
                new_string += chr(new_ascii)
            else:
                new_ascii = ascii_val + 2
                if new_ascii > 122:
                    new_ascii = new_ascii - 122 + 96
                new_string += chr(new_ascii)
        else:
            new_string += char
    return new_string
