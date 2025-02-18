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

    max_word = ''
    max_unique_chars = 0
    for word in words:
        unique_chars = set()
        for char in word:
            if char not in unique_chars:
                unique_chars.add(char)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_chars:
            if max_word > word:
                max_word = word
    return max_word
