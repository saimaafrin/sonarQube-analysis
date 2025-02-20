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

    text = text.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_without_vowels = ''
    for char in text:
        if char not in vowels:
            text_without_vowels += char
    return text_without_vowels
