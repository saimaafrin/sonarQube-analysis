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

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_alphabet = []
    for letter in alphabet:
        new_alphabet.append(letter)
        new_alphabet.append(letter)
    for i in range(2):
        new_alphabet = new_alphabet[1:] + new_alphabet[:1]
    s = s.lower()
    result = ''
    for letter in s:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            result += letter
        else:
            result += new_alphabet[new_alphabet.index(letter)]
    return result
