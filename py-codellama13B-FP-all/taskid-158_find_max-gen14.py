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

    if len(words) == 0:
        return None
    max_string = words[0]
    max_length = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_length:
            max_length = len(unique_chars)
            max_string = word
        elif len(unique_chars) == max_length and word < max_string:
            max_string = word
    return max_string
