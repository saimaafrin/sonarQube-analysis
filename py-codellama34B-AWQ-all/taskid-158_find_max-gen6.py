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


    if not words:
        return None

    max_word = words[0]
    max_char_count = len(set(words[0]))

    for word in words[1:]:
        char_count = len(set(word))
        if char_count > max_char_count:
            max_char_count = char_count
            max_word = word
        elif char_count == max_char_count:
            max_word = min(max_word, word)

    return max_word
