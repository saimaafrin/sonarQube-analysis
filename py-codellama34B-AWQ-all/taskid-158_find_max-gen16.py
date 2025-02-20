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

    max_characters = 0
    word_with_max_characters = words[0]

    for word in words:
        if len(word) == 1:
            continue

        unique_characters = set(word)

        if len(unique_characters) > max_characters:
            max_characters = len(unique_characters)
            word_with_max_characters = word

        elif len(unique_characters) == max_characters:
            if word < word_with_max_characters:
                word_with_max_characters = word

    return word_with_max_characters
