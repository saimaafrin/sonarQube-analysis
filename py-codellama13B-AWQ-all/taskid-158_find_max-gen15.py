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


    max_word = ''
    unique_chars = set()
    for word in words:
        if len(word) > len(max_word):
            max_word = word
            unique_chars = set(word)
        elif len(word) == len(max_word):
            if len(set(word)) > len(unique_chars):
                max_word = word
                unique_chars = set(word)
            elif len(set(word)) == len(unique_chars):
                if word < max_word:
                    max_word = word
                    unique_chars = set(word)
    return max_word
