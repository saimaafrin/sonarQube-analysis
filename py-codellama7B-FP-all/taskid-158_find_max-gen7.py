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

    unique_chars = {}
    max_unique = 0
    max_unique_word = ''
    for word in words:
        if len(word) > max_unique:
            max_unique = len(word)
            max_unique_word = word
        else:
            unique_chars = {}
    for char in max_unique_word:
        if char not in unique_chars:
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1
    for char in unique_chars:
        if unique_chars[char] > max_unique:
            max_unique = unique_chars[char]
    return max_unique_word
