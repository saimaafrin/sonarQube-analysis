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
    text = text.replace('a', '')
    text = text.replace('e', '')
    text = text.replace('i', '')
    text = text.replace('o', '')
    text = text.replace('u', '')
    text = text.replace('y', '')
    return text
