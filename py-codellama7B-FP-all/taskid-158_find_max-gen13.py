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

    unique_chars = set()
    max_length = -1
    max_word = ''
    for word in words:
        length = len(set(word))
        if length == max_length:
            if word < max_word:
                continue
        if length > max_length:
            max_length = length
            max_word = word
    return max_word
