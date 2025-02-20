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

    max_len = 0
    res = ''
    for word in words:
        word_dict = {}
        for ch in word:
            if ch not in word_dict:
                word_dict[ch] = 1
            else:
                word_dict[ch] += 1

        if len(word_dict) > max_len:
            max_len = len(word_dict)
            res = word

    return res
