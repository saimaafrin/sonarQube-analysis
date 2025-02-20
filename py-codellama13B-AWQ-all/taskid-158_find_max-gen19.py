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


    def count_unique(word: str) -> int:
        return len(set(word))

    if not words:
        return None

    unique_count = count_unique(words[0])
    max_word = words[0]

    for word in words[1:]:
        current_count = count_unique(word)
        if current_count > unique_count:
            max_word = word
            unique_count = current_count
        elif current_count == unique_count:
            if word < max_word:
                max_word = word

    return max_word
