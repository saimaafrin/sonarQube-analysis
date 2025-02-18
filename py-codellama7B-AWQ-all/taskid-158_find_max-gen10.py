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
        raise ValueError("Please provide a list of strings")
    if len(words) == 1:
        return words[0]
    else:
        max_unique_chars = 0
        longest_word = ""
        for word in words:
            if len(word) > max_unique_chars:
                max_unique_chars = len(set(word))
                longest_word = word
        return longest_word
