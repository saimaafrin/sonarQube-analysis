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

    unique_words = []
    unique_words_count = 0
    for word in words:
        unique_word = set(word)
        if len(unique_word) > unique_words_count:
            unique_words_count = len(unique_word)
            unique_words = [word]
        elif len(unique_word) == unique_words_count:
            unique_words.append(word)
    unique_words.sort()
    return unique_words[-1]
