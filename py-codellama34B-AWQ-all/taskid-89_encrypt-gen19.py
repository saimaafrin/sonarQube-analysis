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


    enc_str = ''

    for char in s:
        if char.isalpha():
            if char.islower():
                char_num = ord(char) + 2
                if char_num > ord('z'):
                    char_num -= 26
                enc_str += chr(char_num)

            else:
                char_num = ord(char) + 2
                if char_num > ord('Z'):
                    char_num -= 26
                enc_str += chr(char_num)

        else:
            enc_str += char

    return enc_str
