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
        return ""

    current_max: List[str] = []
    for word in words:
        if len(word) > len(current_max):
            current_max = [word]
        elif len(word) == len(current_max):
            current_max.append(word)

    return min(current_max)
