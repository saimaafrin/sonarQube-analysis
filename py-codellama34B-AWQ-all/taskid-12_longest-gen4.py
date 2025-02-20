from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    max_len = len(strings[0]) if strings else 0
    max_index = 0
    for i in range(1, len(strings)):
        if len(strings[i]) > max_len:
            max_len = len(strings[i])
            max_index = i
    return strings[max_index] if max_len > 0 else None
