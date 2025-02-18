def remove_vowels(text: str) -> str:
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for character in text:
        if character.lower() not in vowels:
            new_string += character
    return new_string
