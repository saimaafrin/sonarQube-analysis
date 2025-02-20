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

    # create a dictionary
    d = {}
    for w in words:
        for c in w:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    max_value = 0
    max_key = ''
    for k, v in d.items():
        if v > max_value:
            max_value = v
            max_key = k
    return max_key
