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

    unique_count = {}
    for word in words:
        for ch in word:
            unique_count[ch] = unique_count.get(ch, 0) + 1
    max_word = None
    max_unique = -1
    for word in words:
        unique = 0
        for ch in word:
            unique += unique_count[ch]
        if unique > max_unique:
            max_word = word
            max_unique = unique
    return max_word
