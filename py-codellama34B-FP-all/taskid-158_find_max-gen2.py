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

    max_word = None
    max_len = 0

    for word in words:
        char_set = set(word)
        if len(char_set) > max_len:
            max_len = len(char_set)
            max_word = word
        elif len(char_set) == max_len:
            if word < max_word:
                max_word = word

    return max_word
