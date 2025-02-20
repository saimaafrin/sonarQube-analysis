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

    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        if len(set(words[0])) == len(set(words[1])):
            if words[0] < words[1]:
                return words[1]
            else:
                return words[0]
        else:
            if len(set(words[0])) > len(set(words[1])):
                return words[0]
            else:
                return words[1]

    words.sort(key=lambda x: len(set(x)))
    max_len = len(set(words[0]))
    for word in words:
        if len(set(word)) == max_len:
            return word
    return words[0]
