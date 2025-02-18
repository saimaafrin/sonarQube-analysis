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
        return ""

    def get_unique_chars_count(word: str) -> int:
        return len(set(word))

    max_length = -1
    max_words = []

    for word in words:
        unique_chars_count = get_unique_chars_count(word)

        if unique_chars_count > max_length:
            max_length = unique_chars_count
            max_words = [word]
        elif unique_chars_count == max_length:
            max_words.append(word)

    return sorted(max_words)[0]
