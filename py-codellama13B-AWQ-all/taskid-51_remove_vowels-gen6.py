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
    no_vowels_text = ''
    for character in text:
        if character.lower() not in vowels:
            no_vowels_text += character
    return no_vowels_text
