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

    unique_char_count = {}
    max_unique_count = 0
    max_word = ''

    for word in words:
        unique_chars = set(word)
        unique_char_count[word] = len(unique_chars)
        if len(unique_chars) > max_unique_count:
            max_unique_count = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_count:
            if max_word > word:
                max_word = word

    return max_word
