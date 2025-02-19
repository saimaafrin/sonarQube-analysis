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


    # Your code here
    max_unique_chars = 0
    most_char_word = ""
    for word in words:
        if len(set(word)) > max_unique_chars:
            max_unique_chars = len(set(word))
            most_char_word = word
        elif len(set(word)) == max_unique_chars and word < most_char_word:
            max_unique_chars = len(set(word))
            most_char_word = word
    return most_char_word
