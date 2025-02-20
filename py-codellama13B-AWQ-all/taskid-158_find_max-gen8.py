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

    max_string = words[0]
    max_char_count = 0
    for string in words:
        char_count = len(set(string))
        if char_count > max_char_count or (char_count == max_char_count and string < max_string):
            max_char_count = char_count
            max_string = string
    return max_string
