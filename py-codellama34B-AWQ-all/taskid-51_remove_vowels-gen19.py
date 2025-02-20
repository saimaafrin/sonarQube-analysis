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

    text = list(text)
    for vowel in 'aeiou':
        for i, char in enumerate(text):
            if char.lower() == vowel:
                text.pop(i)
                break
    return ''.join(text)
