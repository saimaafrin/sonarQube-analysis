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

    def count_unique_chars(s):
        return len(set(s))

    def lexicographically_first(s1, s2):
        return s1 < s2

    if len(words) == 0:
        return None
    elif len(words) == 1:
        return words[0]

    max_word = words[0]
    max_unique_chars = count_unique_chars(max_word)
    for word in words[1:]:
        unique_chars = count_unique_chars(word)
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars:
            if lexicographically_first(word, max_word):
                max_word = word

    return max_word
