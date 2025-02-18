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

    unique_chars = set()
    max_chars = -1
    ans = ''
    for word in words:
        if len(word) > max_chars:
            unique_chars = set(word)
            ans = word
        elif len(word) == max_chars:
            if word < ans:
                unique_chars = set(word)
                ans = word
        else:
            unique_chars = unique_chars.union(set(word))
    return ans
