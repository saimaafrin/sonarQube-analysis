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

    if len(words) == 0:
        return ""

    def get_unique_chars(word: str) -> str:
        return "".join(set(word))

    unique_chars: str = get_unique_chars(words[0])
    res: str = words[0]

    for word in words[1:]:
        word_unique_chars: str = get_unique_chars(word)

        if len(word_unique_chars) > len(unique_chars) or (
            len(word_unique_chars) == len(unique_chars) and word < res
        ):
            res = word
            unique_chars = word_unique_chars

    return res
