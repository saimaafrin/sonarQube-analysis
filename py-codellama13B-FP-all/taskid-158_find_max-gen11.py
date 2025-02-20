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

    if not words:
        return None
    if len(words) == 1:
        return words[0]
    max_str = ''
    max_count = -1
    for i, word in enumerate(words):
        if len(word) > max_count:
            max_str = word
            max_count = len(word)
    return max_str
