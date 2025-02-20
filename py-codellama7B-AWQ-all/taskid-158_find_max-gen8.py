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


    word_dict = {}
    for word in words:
        word_dict[word] = len(set(word))

    max_word = ""
    max_count = 0
    for word, count in word_dict.items():
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count and word < max_word:
            max_word = word

    return max_word
