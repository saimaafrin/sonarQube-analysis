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

    max_so_far = 0
    result = words[0]
    for i in range(1, len(words)):
        unique_chars_i = len(set(words[i]))
        if unique_chars_i > max_so_far:
            max_so_far = unique_chars_i
            result = words[i]
        elif unique_chars_i == max_so_far:
            if words[i] < result:
                result = words[i]
    return result
