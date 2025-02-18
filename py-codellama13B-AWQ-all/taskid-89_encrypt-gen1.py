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

    # Builds a new string based on the rotated alphabet
    new_string = ''
    for i in range(len(s)):
        char_index = ord(s[i]) - 97
        char_index = (char_index + 2) % 26
        new_char = chr(char_index + 97)
        new_string += new_char
    return new_string
