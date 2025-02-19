from typing import List

def find_max(words: List[str]) -> str:
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    >>> find_max(['name', 'of', 'string'])
    'string'
    >>> find_max(['name', 'enam', 'game'])
    'enam'
    >>> find_max(['aaaaaaa', 'bb', 'cc'])
    'aaaaaaa'
    """


    word_with_max_char = words[0]
    max_unique_chars = len(set(word_with_max_char))
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            word_with_max_char = word
            max_unique_chars = len(unique_chars)
    return word_with_max_char
