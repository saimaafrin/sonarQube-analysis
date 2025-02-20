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


    max_count = 0
    result = ""

    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            result = word
        elif count == max_count:
            if word < result:
                result = word

    return result
