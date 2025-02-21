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

    # Your code here
    max_word = ''
    max_chars = 0
    for word in words:
        unique_chars = set(word)
        num_chars = len(unique_chars)
        if num_chars > max_chars:
            max_chars = num_chars
            max_word = word
        elif num_chars == max_chars and word < max_word:
            max_word = word

    return max_word
