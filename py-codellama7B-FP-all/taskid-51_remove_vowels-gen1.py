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

    remove_vowels_list = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    for char in remove_vowels_list:
        text = text.replace(char, "")
    return text
