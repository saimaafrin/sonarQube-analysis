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

    max_word = words[0]
    max_characters = len(set(max_word))

    for word in words:
        word_length = len(set(word))
        if word_length > max_characters:
            max_word = word
            max_characters = word_length
        elif word_length == max_characters:
            if word < max_word:
                max_word = word

    return max_word
