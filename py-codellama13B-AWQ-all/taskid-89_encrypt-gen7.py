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

    # create a list of the characters of the string to be encrypted
    string_list = list(s)
    # create a list of the letters of the alphabet
    alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
    # create a list of the rotated letters
    rotated_alphabet_list = [x for x in alphabet_list[2:] + alphabet_list[:2]]
    # create a dictionary that maps each letter to the rotated letter
    rotated_alphabet_dict = dict(zip(alphabet_list, rotated_alphabet_list))
    # create a list of the rotated letters corresponding to the characters in the string
    encrypted_string_list = [rotated_alphabet_dict[char] for char in string_list]
    # return the encrypted string
    return ''.join(encrypted_string_list)
