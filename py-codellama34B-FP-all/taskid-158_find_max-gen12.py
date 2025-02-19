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


    # Find the unique characters of each string and store them in a
    # dictionary
    string_dict = {}
    for string in words:
        string_dict[string] = set(string)

    # Find the maximum length of the sets of characters
    max_len = max([len(string_dict[string]) for string in words])

    # Find the strings with the maximum number of unique characters
    max_strings = [
        string for string in words
        if len(string_dict[string]) == max_len
    ]

    # Return the first string in lexicographical order
    return sorted(max_strings)[0]
