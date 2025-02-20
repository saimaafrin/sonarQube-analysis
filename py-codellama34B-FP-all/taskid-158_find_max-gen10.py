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

    # Your code goes here.
    word = words[0]
    for w in words:
        if len(w) > len(word) and w.lower() != word.lower():
            word = w
        elif len(w) == len(word) and w.lower() != word.lower():
            if w.lower() < word.lower():
                word = w
    return word
