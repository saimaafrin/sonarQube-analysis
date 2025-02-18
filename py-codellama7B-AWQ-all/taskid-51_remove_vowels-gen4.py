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
    text_list = list(text)
    new_text_list = []
    for char in text_list:
        if char not in vowels:
            new_text_list.append(char)
    return ''.join(new_text_list)
