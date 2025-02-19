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

    s_list = list(s)
    new_list = []
    for letter in s_list:
        if letter.isupper():
            if ord(letter) < 68:
                new_list.append(chr(ord(letter) + 20))
            elif ord(letter) > 67 and ord(letter) < 91:
                new_list.append(chr(ord(letter) - 20))
        elif letter.islower():
            if ord(letter) < 100:
                new_list.append(chr(ord(letter) + 20))
            elif ord(letter) > 99 and ord(letter) < 123:
                new_list.append(chr(ord(letter) - 20))
        else:
            new_list.append(letter)
    return "".join(new_list)
