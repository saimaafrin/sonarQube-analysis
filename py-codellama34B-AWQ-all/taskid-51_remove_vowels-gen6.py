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

    vowels = "aeiou"
    text_list = list(text)
    for idx, c in enumerate(text_list):
        if c in vowels:
            text_list.remove(c)
    return "".join(text_list)
