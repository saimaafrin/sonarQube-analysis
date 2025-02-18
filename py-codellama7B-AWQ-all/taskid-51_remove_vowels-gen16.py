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

    # implement your solution here
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for char in text:
        if char.lower() not in vowels:
            res.append(char)
    return ''.join(res)
