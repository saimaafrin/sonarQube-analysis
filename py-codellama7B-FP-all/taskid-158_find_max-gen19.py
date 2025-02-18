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

    # Sort the list by the number of unique characters in each word
    sorted_list = sorted(words, key=lambda x: len(set(x)))
    # Get the maximum number of unique characters
    max_num_unique_chars = len(set(sorted_list[0]))
    # Find the word with the maximum number of unique characters
    word = ''
    for w in sorted_list:
        if len(set(w)) == max_num_unique_chars:
            word = w
            break
    return word
