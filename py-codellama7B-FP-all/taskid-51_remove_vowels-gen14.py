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
    vowels_count = 0
    text_without_vowels = ''
    for letter in text:
        if letter in vowels:
            vowels_count += 1
        else:
            text_without_vowels += letter
    if vowels_count == len(text):
        return ''
    return text_without_vowels
