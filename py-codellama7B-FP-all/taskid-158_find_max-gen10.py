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

    unique_char_count = {}
    for word in words:
        for char in word:
            if char not in unique_char_count:
                unique_char_count[char] = 1
            else:
                unique_char_count[char] += 1

    max_word = ''
    max_char_count = 0
    for word in words:
        char_count = 0
        for char in word:
            if char in unique_char_count:
                char_count += 1
        if char_count > max_char_count or (char_count == max_char_count and word < max_word):
            max_word = word
            max_char_count = char_count

    return max_word
